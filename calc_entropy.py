import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats

# --- 1. Set Font to Arial ---
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Liberation Sans', 'DejaVu Sans', 'sans-serif']

# --- 2. Define Files ---
files = {
    'Sinc Input': 'power_fraction_sinc_input.csv',
    'Sinc Output': 'power_fraction_sinc.csv',
    'Breast Input': 'power_fraction_breast_input.cvs',
    'Breast Output': 'power_fraction_breast.csv',
    'CIFAR Input': 'power_fraction_cifar_input.cvs',
    'CIFAR Output': 'power_fraction_cifar.cvs'
}

# --- 3. Define Custom Palette based on Fig 1, 2, 3 ---
# Extracted colors: Blue for Input, Red for Output
custom_palette = {
    'Output': '#a53a7b',  # Dark Blue from Fig 1
    'Input': '#f06464'  # Salmon Red from Fig 2 & 3
}

# --- 4. Process Data ---
def get_n_modes_90(row):
    """Calculate number of modes for 90% energy"""
    sorted_vals = np.sort(row.values)[::-1]
    cumsum = np.cumsum(sorted_vals)
    if cumsum[-1] < 0.90: return len(row)
    return np.argmax(cumsum >= 0.90) + 1

data_list = []

for label, filepath in files.items():
    try:
        df = pd.read_csv(filepath)
        
        # Calculate Entropy
        entropies = scipy.stats.entropy(df, axis=1)
        
        # Calculate Modes for 90% Energy
        n_modes = df.apply(get_n_modes_90, axis=1)
        
        dataset_name, data_type = label.split(' ')
        
        temp_df = pd.DataFrame({
            'Entropy': entropies,
            'N_Modes': n_modes,
            'Dataset': dataset_name,
            'Type': data_type
        })
        data_list.append(temp_df)
        
    except Exception as e:
        print(f"Error processing {label}: {e}")

full_df = pd.concat(data_list, ignore_index=True)

# --- 5. Plot 1: Entropy Violin Plot ---
plt.figure(figsize=(10, 6))
sns.violinplot(
    data=full_df, 
    x='Dataset', 
    y='Entropy', 
    hue='Type', 
    split=True, 
    inner='quartile', 
    palette=custom_palette
)

#plt.title('Entropy of Modes', fontsize=18)
plt.ylabel('Entropy (nats)', fontsize=22)
plt.xlabel('Dataset', fontsize=22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(title='Type', fontsize=20, title_fontsize=20,  loc='upper right')
#plt.grid(True, axis='y', linestyle='--', alpha=0.6)

plt.savefig('entropy_violin_custom_colors.png', dpi=300, bbox_inches='tight')
plt.show()

# --- 6. Plot 2: Modes 90% Box Plot ---
plt.figure(figsize=(10, 6))
sns.boxplot(
    data=full_df, 
    x='Dataset', 
    y='N_Modes', 
    hue='Type', 
    palette=custom_palette,
    showfliers=True
)

#plt.title('Number of Modes Containing 90% of Energy', fontsize=16)
plt.ylabel('Number of Modes', fontsize=22)
plt.xlabel('Dataset', fontsize=22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(title='Type', fontsize=20, title_fontsize=20)
#plt.grid(True, axis='y', linestyle='--', alpha=0.6)

plt.savefig('modes_boxplot_custom_colors.png', dpi=300, bbox_inches='tight')
plt.show()