import customtkinter as ctk
from tkinter import messagebox
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

# Load the data
gold_data = pd.read_csv("gld_price_data.csv")

# Prepare the data
data = gold_data.drop(['Date'], axis=1)
X = data.drop(['GLD'], axis=1)
Y = data['GLD']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Train the model
regressor = RandomForestRegressor(n_estimators=100)
regressor.fit(X_train, Y_train)

# Function to predict and display results
def predict_price():
    try:
        spx_val = float(spx_entry.get())
        uso_val = float(uso_entry.get())
        slv_val = float(slv_entry.get())
        eur_usd_val = float(eur_usd_entry.get())
        
        # Make prediction
        prediction = regressor.predict([[spx_val, uso_val, slv_val, eur_usd_val]])
        
        # Display result
        result_label.configure(text="Predicted Gold Price: {:.2f}".format(prediction[0]))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values")

# Create GUI
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()
root.title("Gold Price Prediction")

# SPX input
spx_label = ctk.CTkLabel(root, text="SPX:")
spx_label.grid(row=0, column=0, padx=10, pady=5)
spx_entry = ctk.CTkEntry(root)
spx_entry.grid(row=0, column=1, padx=10, pady=5)

# USO input
uso_label = ctk.CTkLabel(root, text="USO:")
uso_label.grid(row=1, column=0, padx=10, pady=5)
uso_entry = ctk.CTkEntry(root)
uso_entry.grid(row=1, column=1, padx=10, pady=5)

# SLV input
slv_label = ctk.CTkLabel(root, text="SLV:")
slv_label.grid(row=2, column=0, padx=10, pady=5)
slv_entry = ctk.CTkEntry(root)
slv_entry.grid(row=2, column=1, padx=10, pady=5)

# EUR/USD input
eur_usd_label = ctk.CTkLabel(root, text="EUR/USD:")
eur_usd_label.grid(row=3, column=0, padx=10, pady=5)
eur_usd_entry = ctk.CTkEntry(root)
eur_usd_entry.grid(row=3, column=1, padx=10, pady=5)

# Predict button
predict_button = ctk.CTkButton(root, text="Predict", command=predict_price)
predict_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Result label
result_label = ctk.CTkLabel(root, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
