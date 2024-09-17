# Usage


## Terminal

```bash
sylabutil-LS45 data_1.asc data_2.asc --outfile ./output.pdf
```

## Script

```python3
import sylabutil.LS45
data = sylabutil.LS45.parse(filepath)
plt.plot(data["wavelength_arr"], data["intensity_arr"])
plt.show()
```