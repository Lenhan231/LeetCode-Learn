import numpy as np
import matplotlib.pyplot as plt

# Generate data
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)

# Create scatter plot with different alpha values
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.scatter(x, y, c=colors, s=sizes, alpha=1.0)
plt.title('alpha=1.0 (opaque)')

plt.subplot(1, 3, 2)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.title('alpha=0.5 (semi-transparent)')

plt.subplot(1, 3, 3)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.1)
plt.title('alpha=0.1 (very transparent)')

plt.tight_layout()
plt.show()
