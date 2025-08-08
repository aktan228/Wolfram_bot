import matplotlib.pyplot as plt 
import numpy as np

class LatexRenderer:
    def __init__(self, fontsize: int = 20, dpi: int = 300):
        self.fontsize = fontsize
        self.dpi = dpi

    def render(self, latex_code: str, filename: str = 'latex.png') -> str:
        fig, ax = plt.subplots(figsize=(0.01, 0.01))
        ax.text(0.5, 0.5, f"${latex_code}$",fontsize=self.fontsize,ha='center', va='center')
        ax.axis('off')
        plt.savefig(filename, dpi=self.dpi,bbox_inches='tight', pad_inches=0.2)
        plt.close(fig)
        return filename