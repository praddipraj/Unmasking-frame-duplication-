import matplotlib.pyplot as plt
import numpy as np

# Data
names = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
methods = ['[4]', '[6]', '[7]', 'Proposed System']
values = [
    [0, 28.34, 44, 34.87],  # No accuracy for Method 1
    [0, 78.88, 92, 88],     # No accuracy for Method 2
    [88, 83, 77, 76],
    [94.3, 91.2, 96.5, 93.8]
]

# Plot
x = np.arange(len(names))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 6))

for i in range(len(methods)):
    bars = ax.bar(x + i*width, values[i], width, label=methods[i])
    if names[i] == 'Accuracy':
        for bar in bars:
            bar.set_label('')  # Remove the label for accuracy bars

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_ylabel('Percentage')
ax.set_title('Comparative Performance Metrics')
ax.set_xticks(x + (len(methods)/2 - 1)*width/2)
ax.set_xticklabels(names, fontsize=40)  # Increase font size for x-axis labels
ax.legend()
ax.grid(True)

fig.tight_layout()

plt.show()
