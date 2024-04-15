from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    
    schedule_data = {
    "4:00 ":   "Wake up",
    "5:00 ":   "Pray",
    "6:00 ":   "Work",
    "7:00 ":   "Work",
    "8:00 ":   "Work",
    "9:00 ":   "Work",
    "10:00 ":  "Work",
    "11:00 ":  "Work",
    "12:00 ":  "Work",
    "13:00 ":  "GYM",
    "14:00 ":  "GYM",
    "15:00 ":  "Lunch With Ian",
    "16:00 ":  "Learn code",
    "17:00 ":  "Learn code",
    "18:00 ":  "Learn code",
    "19:00 ":  "Learn code",
    "20:00 ":  "Learn code",
    "21:00 ":  "Learn code",
    "22:00 ":  "Bedtime routine"
    }
    # Renderiza el template dentro del contexto de la aplicación

    return render_template('index.html', schedule=schedule_data)

# No necesitas imprimir directamente la salida aquí
# La función schedule() será ejecutada automáticamente cuando se haga una solicitud HTTP
if __name__ == "__main__":
    app.run(debug=True)
