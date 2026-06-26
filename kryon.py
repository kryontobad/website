"""
AetherForge Landing Page - Desktop GUI (CustomTkinter)
Windows 11 ready. No browser, no IP, pure desktop app.
"""

import customtkinter as ctk
from PIL import Image, ImageTk  # optional, for actual icons – we'll use emoji as fallback

# -------- Settings --------
ctk.set_appearance_mode("dark")          # "dark", "light", or "system"
ctk.set_default_color_theme("blue")      # base colors, we override some manually

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

# -------- Main App --------
class AetherForgeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("AetherForge")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)
        self.configure(fg_color="#0a0a0a")   # deep black background

        # Center window on screen
        self.center_window()

        # ----- Build UI -----
        self.create_widgets()

        # Optional subtle pulse animation for the CTA button
        self.pulse_state = True
        self.animate_button()

    def center_window(self):
        """Places window at the center of the screen."""
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - WINDOW_WIDTH) // 2
        y = (screen_height - WINDOW_HEIGHT) // 2
        self.geometry(f"+{x}+{y}")

    def create_widgets(self):
        # ---- Top Spacer ----
        ctk.CTkLabel(self, text="", height=40).pack()

        # ---- Brand Name (gradient-like effect using two labels) ----
        # We simulate a gradient by placing two labels: one cyan, one purple, overlapping slightly.
        brand_frame = ctk.CTkFrame(self, fg_color="transparent")
        brand_frame.pack(pady=(20, 0))

        # Cyan part
        self.brand_cyan = ctk.CTkLabel(
            brand_frame,
            text="AETHER",
            font=ctk.CTkFont(family="Orbitron", size=52, weight="bold"),
            text_color="#00e5ff"
        )
        self.brand_cyan.pack(side="left")

        # Purple part
        self.brand_purple = ctk.CTkLabel(
            brand_frame,
            text="FORGE",
            font=ctk.CTkFont(family="Orbitron", size=52, weight="bold"),
            text_color="#b700ff"
        )
        self.brand_purple.pack(side="left")

        # ---- Tagline ----
        self.tagline = ctk.CTkLabel(
            self,
            text="CRAFTING DIGITAL REALITIES",
            font=ctk.CTkFont(family="Inter", size=18, weight="normal"),
            text_color="#a0a0b0"
        )
        self.tagline.pack(pady=(10, 30))

        # ---- CTA Button (with custom hover & glow) ----
        self.cta_button = ctk.CTkButton(
            self,
            text="ENTER THE FORGE",
            font=ctk.CTkFont(family="Inter", size=16, weight="bold"),
            width=250,
            height=50,
            corner_radius=25,
            fg_color="#00e5ff",
            hover_color="#00c4d6",
            text_color="#0a0a0a",
            border_width=0,
            command=self.on_cta_click  # does nothing, just a demo
        )
        self.cta_button.pack(pady=10)

        # ---- Feature Cards (three columns) ----
        cards_frame = ctk.CTkFrame(self, fg_color="transparent")
        cards_frame.pack(pady=50, padx=40, fill="x")

        # Card 1 - Quantum Speed
        self.create_feature_card(cards_frame, "⚡", "Quantum Speed",
                                 "Blazing fast infrastructure\nbuilt for tomorrow.")
        # Card 2 - Ironclad Security
        self.create_feature_card(cards_frame, "🛡️", "Ironclad Security",
                                 "Zero-trust architecture\nkeeping your data safe.")
        # Card 3 - Limitless Scale
        self.create_feature_card(cards_frame, "🌌", "Limitless Scale",
                                 "Expand without boundaries\nacross the metaverse.")

        # ---- Footer ----
        ctk.CTkLabel(
            self,
            text="© 2026 AetherForge — All dimensions reserved.",
            font=ctk.CTkFont(size=12),
            text_color="#555555"
        ).pack(side="bottom", pady=15)

    def create_feature_card(self, parent, icon, title, description):
        """Helper to create a single feature card."""
        card = ctk.CTkFrame(
            parent,
            width=200,
            height=180,
            corner_radius=16,
            fg_color="#111111",
            border_color="#2a2a2a",
            border_width=1
        )
        card.pack(side="left", expand=True, padx=10, pady=10)
        card.pack_propagate(False)  # keep fixed size

        # Icon
        ctk.CTkLabel(
            card,
            text=icon,
            font=ctk.CTkFont(size=32),
            text_color="#00e5ff"
        ).pack(pady=(20, 5))

        # Title
        ctk.CTkLabel(
            card,
            text=title,
            font=ctk.CTkFont(family="Orbitron", size=14, weight="bold"),
            text_color="white"
        ).pack()

        # Description
        ctk.CTkLabel(
            card,
            text=description,
            font=ctk.CTkFont(family="Inter", size=12),
            text_color="#999999",
            justify="center"
        ).pack(pady=(5, 10))

        # Hover effect (change border on enter / leave)
        card.bind("<Enter>", lambda e, c=card: c.configure(border_color="#00e5ff"))
        card.bind("<Leave>", lambda e, c=card: c.configure(border_color="#2a2a2a"))

    def on_cta_click(self):
        """Dummy CTA handler – does nothing but could open something."""
        pass  # replace with actual action if needed

    def animate_button(self):
        """Subtle pulse: alternate between two brightness levels."""
        if self.pulse_state:
            self.cta_button.configure(fg_color="#00e5ff")
        else:
            self.cta_button.configure(fg_color="#00c4d6")
        self.pulse_state = not self.pulse_state
        self.after(600, self.animate_button)  # toggle every 600ms


# -------- Run App --------
if __name__ == "__main__":
    app = AetherForgeApp()
    app.mainloop()
