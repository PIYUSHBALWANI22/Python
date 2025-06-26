"""
Opening files in different modes ('r', 'w', 'a', 'r+', 'w+').

--> Opening files in Python involves specifying the mode in which the file will be accessed. Theoretically, the mode determines the operations that can be performed on the file (reading, writing, appending, or a combination of these).

---

 1. 'r' (Read Mode)
- Purpose: Opens the file for reading only.
- Behavior:
  - The file pointer is placed at the beginning of the file.
  - If the file does not exist, a `FileNotFoundError` is raised.
- Restrictions: Writing to the file is not allowed.

Example:
```
file = open("example.txt", "r")
content = file.read()
file.close()
```


 2. 'w' (Write Mode)
- Purpose: Opens the file for writing only.
- Behavior:
  - Creates a new file if it does not exist.
  - If the file exists, its contents are truncated (erased).
- Restrictions: Reading from the file is not allowed.

Example:
```
file = open("example.txt", "w")
file.write("This will overwrite the file content.")
file.close()
```


 3. 'a' (Append Mode)
- Purpose: Opens the file for appending.
- Behavior:
  - Creates a new file if it does not exist.
  - Data is added to the end of the file without overwriting the existing content.
- Restrictions: Reading from the file is not allowed.

Example:
```
file = open("example.txt", "a")
file.write("This will be added to the end of the file.")
file.close()
```

---

 4. 'r+' (Read and Write Mode)
- Purpose: Opens the file for both reading and writing.
- Behavior:
  - The file pointer is placed at the beginning of the file.
  - Allows both reading and writing operations.
  - The file must exist; otherwise, a `FileNotFoundError` is raised.

Example:
```
file = open("example.txt", "r+")
content = file.read()
file.write("\nAdding more content.")
file.close()
```


 5. 'w+' (Write and Read Mode)
- Purpose: Opens the file for both writing and reading.
- Behavior:
  - Creates a new file if it does not exist.
  - If the file exists, its contents are truncated.
  - Allows both writing and reading operations.

Example:
```
file = open("example.txt", "w+")
file.write("Overwriting content.")
file.seek(0)  # Moves the file pointer to the beginning to read.
content = file.read()
file.close()
```


 Summary of Modes:

| Mode   | Description                         | File Pointer Position | File Creation | Reading Allowed | Writing Allowed |
|--------|-------------------------------------|------------------------|---------------|-----------------|-----------------|
| 'r'  | Read only                         | Beginning              | No            | Yes             | No              |
| 'w'  | Write only (overwrite)            | Beginning              | Yes           | No              | Yes             |
| 'a'  | Append only                       | End                    | Yes           | No              | Yes             |
| 'r+' | Read and write                    | Beginning              | No            | Yes             | Yes             |
| 'w+' | Write and read (overwrite)        | Beginning              | Yes           | Yes             | Yes             |


In theory, selecting the appropriate mode ensures efficient file handling by aligning with the desired operations. Properly closing the file (`file.close()`) after use is essential to release system resources and prevent data corruption. Alternatively, the `with` statement can be used for automatic file management.
"""