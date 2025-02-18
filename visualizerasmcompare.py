import matplotlib.pyplot as plt
import numpy as np

def plot_radar_comparison(metrics1, metrics2, labels):
    # Number of metrics
    num_vars = len(labels)
    
    # Compute angles for radar chart
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Close the polygon
    
    # Prepare data
    def prepare_data(values):
        values = np.array(values)
        values = np.concatenate((values, values[:1]))  # Close the polygon
        return values
    
    data1 = prepare_data(metrics1)
    data2 = prepare_data(metrics2)
    
    # Plot
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'polar': True})
    ax.plot(angles, data1, 'b-', linewidth=2, label='ASM1')
    ax.fill(angles, data1, color='b', alpha=0.25)
    ax.plot(angles, data2, 'r-', linewidth=2, label='ASM2')
    ax.fill(angles, data2, color='r', alpha=0.25)
    
    # Labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_yticklabels([])
    plt.title('ASM Implementation Comparison', pad=20)
    plt.legend()
    plt.show()

# Example usage
labels = [
    'Code Size', 'Control Flow', 'Data Movement', 
    'Computational', 'Memory Access', 'Stack/Heap Ratio',
    'Function Diversity', 'Max Stack'
]

# Assume normalized metrics for ASM1 and ASM2
asm1_metrics = [0.8, 0.2, 0.3, 0.4, 0.1, 1.2, 0.5, 0.6]
asm2_metrics = [0.7, 0.3, 0.4, 0.3, 0.2, 0.8, 0.4, 0.3]

plot_radar_comparison(asm1_metrics, asm2_metrics, labels)