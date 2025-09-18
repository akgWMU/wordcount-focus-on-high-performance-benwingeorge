# Word Frequency Counter with Different Buffering Strategies

A Python script that analyzes **word frequency** across one or more `.txt` files using different **file buffering techniques**.  
It uses a `defaultdict` to efficiently store and update word counts and provides a visualization of the most frequent words.

---

## Features
- **Multiple Buffering Modes**
  - Line-by-line buffered reading  
  - Custom buffer size reading  
  - Character-by-character reading  
- **Efficient Word Counting** using `defaultdict`  
- **Regex-based Word Extraction**  
- **Sorted Display** of word frequencies  
- **Top-N Word Frequency Plotting** using `matplotlib`  

---

## How It Works
**Class: `WordCounter`**
- Uses `defaultdict(int)` to store word counts  
- Normalizes words to lowercase before counting  
- Supports multiple file reading strategies  
- Can process multiple files from a directory  
- Displays sorted word frequencies  
- Plots top-N most frequent words  

---

## Buffering Strategies Explained

### 1. Line-by-Line Buffered Reading
```python
for line in file:
```

- Default buffering provided by Python.
- Efficient for most use cases.
- Reads one line at a time, minimizing memory usage.

### 2. Custom Buffer Size

```python
open(file_path, buffering=buffer_size)
```
- Allows tuning of internal buffer size (e.g., 1024 bytes).
- Useful for performance optimization in specific environments.

### 3. Character-by-Character Reading

```py
file.read(1)
```

- Reads one character at a time.
- Very slow, but demonstrates fine-grained control.
- Not recommended for large files.

## Why Use a Hashmap (defaultdict)?
### Using a hashmap-like structure (defaultdict) offers:

- Constant-time insertion and lookup
- Automatic initialization of missing keys
- Efficient memory usage
- Simplified code compared to manual key checks
- No need to check if word exists — defaultdict handles it.

## Visualization
The script uses matplotlib to plot the top-N most frequent words:

- Bar chart of word frequencies
- Customizable number of top words
- Helps identify dominant vocabulary in the text

## How to Use

1. Place your .txt files in a folder named test_files.
2. Run the script:

```bash
python wordcounter_hashmap.py
```
3. View sorted word counts in the terminal.
4. See a plot of the top 50 words.