# Physics Tutor App

An interactive learning application developed using Python and Streamlit to help learners practise fundamental physics concepts while strengthening the mathematical skills required to understand them.

## About the Project

Physics often requires a strong understanding of mathematics. A learner struggling with a physics concept may actually have difficulty with an underlying mathematical topic.

I developed this application to explore that connection. It combines introductory physics questions with their mathematical prerequisites and uses a rule-based recommendation system to guide learners towards relevant practice.

## Key Features

- **Interactive Practice:** Generates questions across different physics and mathematics topics.
- **Mathematical Prerequisites:** Connects physics topics with relevant mathematical concepts.
- **Adaptive Recommendations:** Recommends prerequisite mathematics practice when a learner answers a physics question incorrectly.
- **Progress Tracking:** Displays practice scores, attempts, accuracy and topic-wise progress during a session.
- **Instant Feedback:** Provides feedback and explanations after answers are submitted.
- **Randomised Questions:** Generates different numerical problems for repeated practice.

## Topics Covered

### Physics
- Kinematics
- Newton's Laws of Motion
- Work, Energy and Power
- Rotational Motion
- Simple Harmonic Motion
- Current Electricity

### Mathematics
- Quadratic Equations
- Calculus (Integration)
- Vector Algebra (Dot Product)
- Vector Algebra (Cross Product)
- Trigonometry and Sinusoids
- Logarithms and Exponential Functions

## Technologies Used

- **Python:** Core application logic and problem generation.
- **Streamlit:** Interactive web application interface.
- **SymPy:** Mathematical computation and symbolic mathematics.

## How the Recommendation System Works

The application uses a predefined relationship between physics topics and their mathematical prerequisites.

When a learner answers a physics question incorrectly, the application recommends practising the corresponding mathematical prerequisite. After successful prerequisite practice, the learner can return to physics questions.

This is a rule-based learning approach designed to encourage stronger mathematical foundations.

## Live Application

Try the application here:

[Physics Tutor App](https://physics-tutor-app.streamlit.app/)

## Running Locally

1. Clone this repository:

```bash
git clone https://github.com/Titan-Earth/Physics_Tutor_App.git
```

2. Open the project directory:

```bash
cd Physics_Tutor_App
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app.py
```

## Learning Outcomes

Through this project, I explored:

- Applying Python to develop an interactive educational application.
- Generating mathematical problems programmatically.
- Using mathematical relationships to structure a learning pathway.
- Building a web interface with Streamlit.
- Connecting mathematical foundations with physics problem-solving.

---

**Developed as an independent programming and educational project.**
