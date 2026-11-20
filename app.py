import random
import math
import sqlite3
from datetime import datetime

import streamlit as st
import sympy as sp

# Define the symbolic variable used in calculus questions
x = sp.Symbol("x")

# --- 1. DATABASE FUNCTIONS ---

DB_NAME = "progress.db"


def init_db():
    """Create the progress table if it does not already exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            topic TEXT,
            score INTEGER
        )
        """
    )

    conn.commit()
    conn.close()


def save_score(topic, score):
    """Save one attempt to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO progress (timestamp, topic, score)
        VALUES (?, ?, ?)
        """,
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), topic, score),
    )

    conn.commit()
    conn.close()


def load_history():
    """Return all saved progress records, oldest first."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT timestamp, topic, score
        FROM progress
        ORDER BY id ASC
        """
    )

    rows = cursor.fetchall()
    conn.close()

    return rows


def reset_history():
    """Delete all saved progress records."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM progress")

    conn.commit()
    conn.close()


# --- 2. SYLLABUS GRAPH ---

SYLLABUS_GRAPH = {
    "Kinematics (Motion in 1D)": {
        "prerequisite": "Quadratic Equations",
    },
    "Newton's Laws of Motion": {
        "prerequisite": "Vector Algebra (Dot Product)",
    },
    "Work, Energy & Power": {
        "prerequisite": "Calculus (Integration)",
    },
    "Rotational Motion": {
        "prerequisite": "Vector Algebra (Cross Product)",
    },
    "Simple Harmonic Motion": {
        "prerequisite": "Trigonometry & Sinusoids",
    },
    "Current Electricity": {
        "prerequisite": "Logarithms & Exponential Functions",
    },

    # Math prerequisite nodes
    "Quadratic Equations": {
        "prerequisite": None,
    },
    "Calculus (Integration)": {
        "prerequisite": None,
    },
    "Vector Algebra (Dot Product)": {
        "prerequisite": None,
    },
    "Vector Algebra (Cross Product)": {
        "prerequisite": None,
    },
    "Trigonometry & Sinusoids": {
        "prerequisite": None,
    },
    "Logarithms & Exponential Functions": {
        "prerequisite": None,
    },
}

PHYSICS_TOPICS = [
    "Kinematics (Motion in 1D)",
    "Newton's Laws of Motion",
    "Work, Energy & Power",
    "Rotational Motion",
    "Simple Harmonic Motion",
    "Current Electricity",
]


# --- 3. QUESTION GENERATOR ---

def generate_problem(topic):
    """Generate one randomized question, answer, and solution."""

    if topic == "Kinematics (Motion in 1D)":
        u = random.randint(2, 10)
        a = random.randint(1, 5)
        t = random.randint(2, 6)

        ans = float(u * t + 0.5 * a * t**2)

        question = (
            "Physics: A particle starts with initial velocity "
            f"{u} m/s and has a constant acceleration of {a} m/s². "
            f"Find its displacement after {t} seconds."
        )

        steps = (
            "1. Formula: $s = ut + \\frac{1}{2}at^2$\n"
            f"2. Substitute: $s = ({u})({t}) + \\frac{{1}}{{2}}({a})({t})^2$\n"
            f"3. Calculate: $s = {ans}$ m"
        )

        return question, ans, steps

    elif topic == "Newton's Laws of Motion":
        m = random.randint(2, 10)
        f = random.randint(10, 50)

        ans = float(f / m)

        question = (
            "Physics: A force of "
            f"{f} N is applied to an object of mass {m} kg. "
            "Find its acceleration."
        )

        steps = (
            "1. Formula: $F = ma$\n"
            "2. Rearrange: $a = \\frac{F}{m}$\n"
            f"3. Calculate: $a = \\frac{{{f}}}{{{m}}} = {ans}$ m/s²"
        )

        return question, ans, steps

    elif topic == "Work, Energy & Power":
        f = random.randint(5, 20)
        d = random.randint(2, 10)

        ans = float(f * d)

        question = (
            "Physics: A constant force of "
            f"{f} N moves an object by {d} m in the direction of the force. "
            "Find the work done."
        )

        steps = (
            "1. Formula: $W = Fd$\n"
            f"2. Calculate: $W = ({f})({d}) = {ans}$ J"
        )

        return question, ans, steps

    elif topic == "Rotational Motion":
        force = random.randint(2, 10)
        radius = random.randint(1, 5)

        ans = float(force * radius)

        question = (
            "Physics: A force of "
            f"{force} N is applied tangentially at a distance of {radius} m "
            "from the axis of rotation. Find the torque."
        )

        steps = (
            "1. Formula: $\\tau = rF$\n"
            f"2. Calculate: $\\tau = ({radius})({force}) = {ans}$ N·m"
        )

        return question, ans, steps

    elif topic == "Simple Harmonic Motion":
        amp = random.randint(2, 10)
        omega = random.randint(1, 5)
        t = random.randint(1, 5)

        ans = round(amp * math.sin(omega * t), 2)

        question = (
            "Physics: A particle performs simple harmonic motion with "
            f"amplitude {amp} m and angular frequency {omega} rad/s. "
            f"Find its displacement at t = {t} s, assuming "
            "$x(t) = A\\sin(\\omega t)$."
        )

        steps = (
            "1. Formula: $x(t) = A\\sin(\\omega t)$\n"
            f"2. Substitute: $x = {amp}\\sin(({omega})({t}))$\n"
            f"3. Calculate: $x = {ans}$ m"
        )

        return question, ans, steps

    elif topic == "Current Electricity":
        v = random.randint(5, 24)
        r = random.randint(2, 12)

        ans = round(v / r, 2)

        question = (
            "Physics: A voltage of "
            f"{v} V is applied across a resistor of {r} Ω. "
            "Find the current flowing through it."
        )

        steps = (
            "1. Formula: $I = \\frac{V}{R}$\n"
            f"2. Calculate: $I = \\frac{{{v}}}{{{r}}} = {ans}$ A"
        )

        return question, ans, steps

    elif topic == "Quadratic Equations":
        root = random.randint(1, 8)

        ans = float(root)

        question = (
            "Math Prerequisite (Algebra): Solve for $x$: "
            f"$(x - {root})^2 = 0$."
        )

        steps = (
            "1. Take the square root: $x - "
            f"{root} = 0$\n"
            f"2. Solve: $x = {root}$"
        )

        return question, ans, steps

    elif topic == "Calculus (Integration)":
        a, b = random.randint(2, 6), random.randint(1, 8)
        x_val = random.randint(1, 3)

        f_expr = a * x + b
        ans = float(sp.integrate(f_expr, (x, 0, x_val)))

        question = (
            "Math Prerequisite (Calculus): Evaluate\n"
            f"$\\int_{{0}}^{{{x_val}}} ({sp.latex(f_expr)}) \\, dx$"
        )

        steps = (
            "1. Integrate:\n"
            f"$\\left[{sp.latex(sp.integrate(f_expr, x))}\\right]_0^{{{x_val}}}$\n"
            f"2. Evaluate: {ans}"
        )

        return question, ans, steps

    elif topic == "Vector Algebra (Dot Product)":
        a1, a2 = random.randint(1, 7), random.randint(1, 7)
        b1, b2 = random.randint(1, 7), random.randint(1, 7)

        ans = float(a1 * b1 + a2 * b2)

        question = (
            "Math Prerequisite (Vectors): Find the scalar (dot) product "
            "$\\vec{A} \\cdot \\vec{B}$ if "
            f"$\\vec{{A}} = {a1}\\hat{{i}} + {a2}\\hat{{j}}$ and "
            f"$\\vec{{B}} = {b1}\\hat{{i}} + {b2}\\hat{{j}}$."
        )

        steps = (
            "1. Formula: "
            "$\\vec{A} \\cdot \\vec{B} = A_xB_x + A_yB_y$\n"
            f"2. Calculate: $({a1})({b1}) + ({a2})({b2}) = {ans}$"
        )

        return question, ans, steps

    elif topic == "Vector Algebra (Cross Product)":
        ax, ay = random.randint(2, 6), random.randint(1, 5)
        bx, by = random.randint(1, 5), random.randint(2, 6)

        ans = float(ax * by - ay * bx)

        question = (
            "Math Prerequisite (Vectors): Find the $\\hat{k}$ coefficient of "
            "$\\vec{A} \\times \\vec{B}$ for "
            f"$\\vec{{A}} = {ax}\\hat{{i}} + {ay}\\hat{{j}}$ and "
            f"$\\vec{{B}} = {bx}\\hat{{i}} + {by}\\hat{{j}}$."
        )

        steps = (
            "1. Determinant rule: "
            "$(\\vec{A} \\times \\vec{B})_z = A_xB_y - A_yB_x$\n"
            f"2. Calculate: $({ax})({by}) - ({ay})({bx}) = {ans}$"
        )

        return question, ans, steps

    elif topic == "Trigonometry & Sinusoids":
        amp = random.randint(5, 25)
        deg = random.choice([30, 45, 60, 90])

        ans = round(amp * math.sin(math.radians(deg)), 2)

        question = (
            "Math Prerequisite (Trigonometry): Evaluate "
            f"$f(\\theta) = {amp}\\sin(\\theta)$ when "
            f"$\\theta = {deg}^\\circ$."
        )

        steps = (
            "1. Standard value: "
            f"$\\sin({deg}^\\circ) = "
            f"{round(math.sin(math.radians(deg)), 3)}$\n"
            f"2. Multiply: ${amp} \\times \\sin({deg}^\\circ) = {ans}$"
        )

        return question, ans, steps

    elif topic == "Logarithms & Exponential Functions":
        base = 2
        power = random.randint(2, 5)
        val = base**power

        ans = float(power)

        question = (
            "Math Prerequisite (Logarithms): Solve for $x$: "
            f"$2^x = {val}$, i.e. evaluate $\\log_2({val})$."
        )

        steps = (
            f"1. Rewrite as a power: ${val} = 2^{{{power}}}$\n"
            "2. Apply the logarithm definition: "
            f"$\\log_2(2^{{{power}}}) = {power}$"
        )

        return question, ans, steps

    # Fallback in case an unknown topic is selected
    question = "Question generator not available for this topic."
    steps = "Please select a valid topic."
    return question, 0.0, steps


# --- 4. STREAMLIT INTERFACE ---

st.set_page_config(
    page_title="Adaptive STEM Gap Analyzer",
    page_icon="🧠",
)

st.title("🧠 Adaptive Physics & Math Gap Analyzer")
st.markdown(
    "Full Class 12 Diagnostic Engine with Persistent SQLite Progress Tracking."
)

# Initialize the database
init_db()

# Load saved progress
saved_rows = load_history()
saved_scores = [row[2] for row in saved_rows]

# Initialize session state
if "current_topic" not in st.session_state:
    st.session_state.current_topic = random.choice(PHYSICS_TOPICS)

if "q_data" not in st.session_state:
    st.session_state.q_data = generate_problem(st.session_state.current_topic)

if "mastery_score" not in st.session_state:
    st.session_state.mastery_score = (
        saved_scores[-1] if saved_scores else 40
    )


# Sidebar
with st.sidebar:
    st.header("📊 Permanent Improvement Tracker")

    st.metric(
        label="Current Mastery Rating",
        value=f"{st.session_state.mastery_score}/100",
    )

    if len(saved_scores) > 1:
        st.subheader("Saved Growth Trajectory")
        st.line_chart(saved_scores)
    else:
        st.info(
            "Answer at least 2 questions to plot your saved curve!"
        )

    st.divider()

    st.subheader("🎯 Practice Mode")

    selected_topic = st.selectbox(
        "Jump to a specific chapter (optional):",
        ["-- Adaptive Auto-Mode --"] + list(SYLLABUS_GRAPH.keys()),
    )

    if selected_topic != "-- Adaptive Auto-Mode --":
        if st.button("Load Selected Chapter"):
            st.session_state.current_topic = selected_topic
            st.session_state.q_data = generate_problem(selected_topic)
            st.rerun()

    st.divider()

    st.subheader("🕸️ Active Knowledge Node")
    st.write(f"Current Topic: {st.session_state.current_topic}")

    prereq = SYLLABUS_GRAPH[st.session_state.current_topic]["prerequisite"]
    st.write(f"Underlying Math Skill: {prereq}")

    st.divider()

    if st.button("🗑️ Reset Saved Progress"):
        reset_history()
        st.session_state.mastery_score = 40
        st.rerun()


# Main quiz area
question_text, correct_answer, solution_steps = st.session_state.q_data

st.subheader(f"Topic: {st.session_state.current_topic}")
st.info(question_text)

user_input = st.number_input(
    "Enter your numerical answer (round to 2 decimal places if needed):",
    step=0.1,
    format="%.2f",
    key="user_ans",
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Submit Answer", type="primary", key="submit_btn"):

        if abs(user_input - correct_answer) <= 0.15:
            st.success("✅ Correct! Score saved to database.")

            st.session_state.mastery_score = min(
                100,
                st.session_state.mastery_score + 10,
            )

            save_score(
                st.session_state.current_topic,
                st.session_state.mastery_score,
            )

            if st.session_state.current_topic not in PHYSICS_TOPICS:
                st.toast(
                    "Math prerequisite mastered! Returning to Physics..."
                )
                st.session_state.current_topic = random.choice(
                    PHYSICS_TOPICS
                )

            with st.expander("View Step-by-Step Symbolic Solution"):
                st.markdown(solution_steps)

        else:
            st.error(
                f"❌ Incorrect. The exact answer is {correct_answer}."
            )

            st.session_state.mastery_score = max(
                0,
                st.session_state.mastery_score - 5,
            )

            save_score(
                st.session_state.current_topic,
                st.session_state.mastery_score,
            )

            weak_math_node = SYLLABUS_GRAPH[
                st.session_state.current_topic
            ]["prerequisite"]

            if weak_math_node in SYLLABUS_GRAPH:
                st.warning(
                    "🔍 Diagnostic Alert: Failure traced to prerequisite "
                    f"node: {weak_math_node}. Adapting next question..."
                )

                st.session_state.current_topic = weak_math_node

            with st.expander(
                "View Step-by-Step Symbolic Solution",
                expanded=True,
            ):
                st.markdown(solution_steps)

with col2:
    if st.button("Next Question ➡️", key="next_btn"):
        st.session_state.q_data = generate_problem(
            st.session_state.current_topic
        )
        st.rerun()


# Detailed progress table
st.divider()

with st.expander("📜 View Detailed Progress Log"):
    if saved_rows:
        st.table(
            [
                {
                    "Date & Time": row[0],
                    "Chapter / Topic": row[1],
                    "Score": row[2],
                }
                for row in saved_rows
            ]
        )
    else:
        st.write(
            "No questions attempted yet. Submit an answer above to start "
            "logging!"
        )
