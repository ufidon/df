# Build wxHexEditor

```bash
# 1. removed installed wxHexEditor
sudo apt purge wxhexeditor

```

* Download wxHexEditor from [here](./tools/wxHexEditor/)
* Check file integrity
* Extract the prebuilt *wxHexEditor* in the build folder
```bash
# 2. extract wxHexEditor
7z x wxhexeditor.7z

```

## References
* [wxHexEditor](https://www.wxhexeditor.org)
  * [wxHexEditor source code](https://github.com/EUA/wxHexEditor)
* [xwHexEditor does not compile](https://github.com/EUA/wxHexEditor/issues/150)
* [wxYield called recursively](https://github.com/EUA/wxHexEditor/issues/113)