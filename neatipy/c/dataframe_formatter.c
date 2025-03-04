#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

static PyObject *format_dataframe(PyObject *self, PyObject *args)
{
    const int PADDING = 2; // how much extra space around the data/columns
    PyObject *cols, *data;
    if (!PyArg_ParseTuple(args, "O!O!", &PyList_Type, &cols, &PyList_Type, &data))
    {
        PyErr_SetString(PyExc_TypeError, "Both parameters must be lists.");
        return NULL;
    }

    Py_ssize_t cols_len = PyList_Size(cols);
    Py_ssize_t data_len = PyList_Size(data);

    /* Allocate an array for the maximum width for each column.
       Initialize each column’s width to the length of its header plus PADDING. */
    int *longest_datas = malloc(cols_len * sizeof(int));
    if (longest_datas == NULL)
    {
        PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory for longest_datas.");
        return NULL;
    }
    for (Py_ssize_t j = 0; j < cols_len; j++)
    {
        PyObject *col = PyList_GetItem(cols, j);
        PyObject *str_obj = PyObject_Str(col);
        if (!str_obj)
        {
            free(longest_datas);
            PyErr_SetString(PyExc_TypeError, "Failed to convert column name to string.");
            return NULL;
        }
        const char *col_str = PyUnicode_AsUTF8(str_obj);
        if (!col_str)
        {
            Py_DECREF(str_obj);
            free(longest_datas);
            PyErr_SetString(PyExc_TypeError, "Failed to get UTF-8 string for column name.");
            return NULL;
        }
        longest_datas[j] = (int)strlen(col_str) + PADDING;
        Py_DECREF(str_obj);
    }

    /* Ensure each row in data is a list of the proper length and update longest_datas */
    if (data_len > 0)
    {
        PyObject *first_row = PyList_GetItem(data, 0);
        if (!PyList_Check(first_row))
        {
            free(longest_datas);
            PyErr_SetString(PyExc_TypeError, "Each element in data must be a list.");
            return NULL;
        }
        if (PyList_Size(first_row) != cols_len)
        {
            free(longest_datas);
            PyErr_SetString(PyExc_TypeError, "Number of columns does not match the number of elements in data rows.");
            return NULL;
        }
    }
    for (Py_ssize_t i = 0; i < data_len; i++)
    {
        PyObject *row = PyList_GetItem(data, i);
        if (!PyList_Check(row))
        {
            free(longest_datas);
            PyErr_SetString(PyExc_TypeError, "Each element in data must be a list.");
            return NULL;
        }
        if (PyList_Size(row) != cols_len)
        {
            free(longest_datas);
            PyErr_SetString(PyExc_TypeError, "Row length does not match number of columns.");
            return NULL;
        }
        for (Py_ssize_t j = 0; j < cols_len; j++)
        {
            PyObject *item = PyList_GetItem(row, j);
            PyObject *str_obj = PyObject_Str(item);
            if (!str_obj)
            {
                free(longest_datas);
                PyErr_SetString(PyExc_TypeError, "Failed to convert data item to string.");
                return NULL;
            }
            const char *c_str = PyUnicode_AsUTF8(str_obj);
            if (!c_str)
            {
                Py_DECREF(str_obj);
                free(longest_datas);
                PyErr_SetString(PyExc_TypeError, "Failed to get UTF-8 string for data item.");
                return NULL;
            }
            int length = (int)strlen(c_str);
            if (length + PADDING > longest_datas[j])
            {
                longest_datas[j] = length + PADDING;
            }
            Py_DECREF(str_obj);
        }
    }

    /* Calculate total table width.
       Each cell will be printed with its content (width longest_datas[j])
       and wrapped with a leading and trailing "|" (adding 2 characters per column). */
    int table_width = 0;
    for (Py_ssize_t j = 0; j < cols_len; j++)
    {
        table_width += longest_datas[j] + 2;
    }

    /* Prepare an output buffer and track the used size manually */
    unsigned long long buffer_size = 4096;
    unsigned long long used_size = 0;
    char *buffer = malloc(buffer_size);
    if (!buffer)
    {
        free(longest_datas);
        PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory for buffer.");
        return NULL;
    }
    buffer[0] = '\0';

    /* Build top border line (a single continuous line of '-' for the whole width) */
    while (buffer_size < used_size + table_width + 2)
    {
        buffer_size *= 2;
        buffer = realloc(buffer, buffer_size);
        if (!buffer)
        {
            free(longest_datas);
            PyErr_SetString(PyExc_MemoryError, "Failed to reallocate buffer");
            return NULL;
        }
    }
    char *border = malloc(table_width + 2);
    if (!border)
    {
        free(buffer);
        free(longest_datas);
        PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory for border");
        return NULL;
    }
    memset(border, '-', table_width);
    border[table_width] = '\n';
    border[table_width + 1] = '\0';

    size_t borderlen = strlen(border);
    memcpy(buffer + used_size, border, borderlen);
    used_size += borderlen;
    buffer[used_size] = '\0';

    for (Py_ssize_t j = 0; j < cols_len; j++)
    {
        while (buffer_size < used_size + 2)
        {
            buffer_size *= 2;
            buffer = realloc(buffer, buffer_size);
            if (!buffer)
            {
                free(longest_datas);
                PyErr_SetString(PyExc_MemoryError, "Failed to reallocate buffer");
                return NULL;
            }
        }
        {
            const char *s = "|";
            size_t len = strlen(s);
            memcpy(buffer + used_size, s, len);
            used_size += len;
            buffer[used_size] = '\0';
        }

        int content_width = longest_datas[j];
        char *cell = malloc(content_width + 1);
        if (!cell)
        {
            free(buffer);
            free(longest_datas);
            PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory for header cell");
            return NULL;
        }
        memset(cell, ' ', content_width);
        cell[content_width] = '\0';

        PyObject *col_obj = PyList_GetItem(cols, j);
        PyObject *str_obj = PyObject_Str(col_obj);
        if (!str_obj)
        {
            free(cell);
            free(buffer);
            free(longest_datas);
            PyErr_SetString(PyExc_TypeError, "Failed to convert column name to string.");
            return NULL;
        }
        const char *col_str = PyUnicode_AsUTF8(str_obj);
        if (!col_str)
        {
            Py_DECREF(str_obj);
            free(cell);
            free(buffer);
            free(longest_datas);
            PyErr_SetString(PyExc_TypeError, "Failed to get UTF-8 string for column name.");
            return NULL;
        }
        int name_len = (int)strlen(col_str);
        int padding = content_width - name_len;
        int pad_left = padding / 2;
        memcpy(cell + pad_left, col_str, name_len);
        Py_DECREF(str_obj);

        while (buffer_size < used_size + content_width + 2)
        {
            buffer_size *= 2;
            buffer = realloc(buffer, buffer_size);
            if (!buffer)
            {
                free(cell);
                free(longest_datas);
                PyErr_SetString(PyExc_MemoryError, "Failed to reallocate buffer");
                return NULL;
            }
        }
        {
            size_t len = strlen(cell);
            memcpy(buffer + used_size, cell, len);
            used_size += len;
            buffer[used_size] = '\0';
        }
        {
            const char *s = "|";
            size_t len = strlen(s);
            memcpy(buffer + used_size, s, len);
            used_size += len;
            buffer[used_size] = '\0';
        }
        free(cell);
    }
    {
        const char *s = "\n";
        size_t len = strlen(s);
        memcpy(buffer + used_size, s, len);
        used_size += len;
        buffer[used_size] = '\0';
    }

    while (buffer_size < used_size + table_width + 2)
    {
        buffer_size *= 2;
        buffer = realloc(buffer, buffer_size);
        if (!buffer)
        {
            free(longest_datas);
            PyErr_SetString(PyExc_MemoryError, "Failed to reallocate buffer");
            return NULL;
        }
    }

    memcpy(buffer + used_size, border, borderlen);
    used_size += borderlen;
    buffer[used_size] = '\0';

    /* Build data rows with centered values */
    for (Py_ssize_t i = 0; i < data_len; i++)
    {
        PyObject *row = PyList_GetItem(data, i);
        for (Py_ssize_t j = 0; j < cols_len; j++)
        {
            while (buffer_size < used_size + 2)
            {
                buffer_size *= 2;
                buffer = realloc(buffer, buffer_size);
                if (!buffer)
                {
                    free(longest_datas);
                    PyErr_SetString(PyExc_MemoryError, "Failed to reallocate buffer");
                    return NULL;
                }
            }
            {
                const char *s = "|";
                size_t len = strlen(s);
                memcpy(buffer + used_size, s, len);
                used_size += len;
                buffer[used_size] = '\0';
            }

            int content_width = longest_datas[j];
            char *cell = malloc(content_width + 1);
            if (!cell)
            {
                free(border);
                free(buffer);
                free(longest_datas);
                PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory for data cell");
                return NULL;
            }
            memset(cell, ' ', content_width);
            cell[content_width] = '\0';

            PyObject *item = PyList_GetItem(row, j);
            PyObject *str_obj = PyObject_Str(item);
            if (!str_obj)
            {
                free(border);
                free(cell);
                free(buffer);
                free(longest_datas);
                PyErr_SetString(PyExc_TypeError, "Failed to convert data item to string.");
                return NULL;
            }
            const char *data_str = PyUnicode_AsUTF8(str_obj);
            if (!data_str)
            {
                Py_DECREF(str_obj);
                free(cell);
                free(buffer);
                free(longest_datas);
                PyErr_SetString(PyExc_TypeError, "Failed to get UTF-8 string for data item.");
                return NULL;
            }
            int data_len_item = (int)strlen(data_str);
            if (data_len_item > content_width)
                data_len_item = content_width;
            int padding = content_width - data_len_item;
            int pad_left = padding / 2;
            memcpy(cell + pad_left, data_str, data_len_item);
            Py_DECREF(str_obj);

            while (buffer_size < used_size + content_width + 2)
            {
                buffer_size *= 2;
                buffer = realloc(buffer, buffer_size);
                if (!buffer)
                {
                    free(cell);
                    free(longest_datas);
                    PyErr_SetString(PyExc_MemoryError, "Failed to reallocate buffer");
                    return NULL;
                }
            }
            {
                size_t len = strlen(cell);
                memcpy(buffer + used_size, cell, len);
                used_size += len;
                buffer[used_size] = '\0';
            }
            {
                const char *s = "|";
                size_t len = strlen(s);
                memcpy(buffer + used_size, s, len);
                used_size += len;
                buffer[used_size] = '\0';
            }
            free(cell);
        }
        {
            const char *s = "\n";
            size_t len = strlen(s);
            memcpy(buffer + used_size, s, len);
            used_size += len;
            buffer[used_size] = '\0';
        }
    }

    /* Build bottom border line (same as the top border) */
    while (buffer_size < used_size + table_width + 2)
    {
        buffer_size *= 2;
        buffer = realloc(buffer, buffer_size);
        if (!buffer)
        {
            free(border);
            free(longest_datas);
            PyErr_SetString(PyExc_MemoryError, "Failed to reallocate buffer");
            return NULL;
        }
    }

    memcpy(buffer + used_size, border, borderlen);
    used_size += borderlen;
    buffer[used_size] = '\0';

    free(border);
    PyObject *result = PyUnicode_FromString(buffer);
    free(buffer);
    free(longest_datas);
    return result;
}

// Method definitions
static PyMethodDef CMethods[] = {
    {"format_dataframe", format_dataframe, METH_VARARGS, "Return formatted pandas dataframe"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef c_module = {
    PyModuleDef_HEAD_INIT,
    "neatipy_c",
    "A C extension for neatipy, for performance heavy operations",
    -1,
    CMethods};

PyMODINIT_FUNC PyInit_neatipy_c(void)
{
    return PyModule_Create(&c_module);
}
