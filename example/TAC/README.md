# Usage


## Terminal

```bash
sylabutil-TAC data_1.asc data_2.asc --outfile ./output.pdf
```

## Script

```python3
import sylabutil.TAC
filedata = sylabutil.TAC.parse(filepath)
block = filedata["block"]
times = block["1"]["Time[ns]"]
values = block["1"]["No_of_photons"]

plt.plot(times, values)
plt.xlabel("Time[ns]")
plt.ylabel("No_of_photons")
plt.show()
```
