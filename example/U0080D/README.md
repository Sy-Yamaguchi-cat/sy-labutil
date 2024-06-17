# Usage


## Terminal

```bash
sylabutil-U0080D data_1.xls data_2.xls --outfile ./output.pdf
```

## Script

```python3
import sylabutil.U0080D
fileinfo = sylabutil.U0080D.parse(filepath)
data = fileinfo["data"]
print(f"n: {fileinfo['points']}")

plt.plot(data["wavelength"], data["value"])
plt.show()
```
