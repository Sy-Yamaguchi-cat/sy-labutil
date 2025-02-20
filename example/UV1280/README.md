# Usage

## Terminal

```bash
sylabutil-UV1280 data_1.csv data_2.csv --outfile ./output.pdf
```

## Script

```python3
import matplotlib.pyplot as plt
import sylabutil.UV1280
data = sylabutil.UV1280.parse(filepath)

print(f"{data['title']}")

plt.plot(data["wavelength"], data["transmittance"])
plt.show()
```
