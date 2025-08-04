# Introduction to Machine Learning and Its Application to Gaming

This project introduces fundamental machine learning (ML) concepts through hands-on, game-based assignments. By developing rule-based agents, collecting gameplay data, and applying both supervised and reinforcement learning, we explore how machines can learn to play games and improve their behavior over time.

Originally developed as part of a course at National Cheng Kung University (NCKU), the project emphasizes the transition from manual rule-based logic to intelligent decision-making systems.

---

## Table of Contents

1. [Project Pipeline](#1-project-pipeline)  
2. [Game Modules Overview](#2-game-modules-overview)  
3. [Tools and Technologies](#3-tools-and-technologies)  
4. [Project Structure](#4-project-structure)  
5. [Key Learnings](#5-key-learnings)  
6. [Future Directions](#6-future-directions)  
7. [Author](#7-author)

---

## 1. Project Pipeline

The overall development process follows these steps:

- **Rule-Based Agent Creation**  
  Write hardcoded agents that play the games using simple decision logic.

- **Data Collection via Gameplay**  
  Run rule-based agents to collect `.pickle` data logs from game frames.

- **Feature Extraction & Dataset Creation**  
  Convert raw gameplay data into structured features such as positions, velocities, and directions.

- **Model Training & Evaluation**  
  Train ML models such as K-Nearest Neighbors (KNN) and Random Forest on the extracted features.

- **Reinforcement Learning (Advanced)**  
  Implement Q-learning to allow agents to learn strategies through trial and error without labeled data.

---

## 2. Game Modules Overview

### Game 1: Brick Breaker

- **Method**: Supervised Learning (KNN)  
- **Goal**: Predict paddle movement based on the ball’s trajectory  
- **Outcome**: The KNN model mimics the rule-based logic accurately in most scenarios

---

### Game 2: Ping Pong

- **Enhancement**: Improved the rule agent by adding delays and better paddle control  
- **Models Tried**: KNN and Random Forest  
- **Result**: KNN proved more stable and effective than Random Forest in this task

---

### Game 3: Snake

- **Challenge**: Rule-based agent can nearly solve the game, limiting diversity in training data  
- **Strategy**: Selected only a few datasets to avoid overfitting  
- **Model**: KNN  
- **Insight**: Even simple models can perform well, but only with carefully chosen training data

---

### Game 4: CartPole (Reinforcement Learning)

- **Approach**: Q-learning  
- **Objective**: Balance a pole on a cart by learning action values over time  
- **Key Insight**: Reinforcement learning allows agents to learn from rewards instead of explicit labels

---

## 3. Tools and Technologies

- Python
- Scikit-learn – KNN, Random Forest
- OpenAI Gym – CartPole environment
- NumPy, Matplotlib – Data manipulation and visualization
- Pickle – Model and data serialization

---

## 4. Project Structure

| Folder               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `HW1_Brick_Breaker/` | Brick Breaker implementation using rule-based and KNN agents. Includes training and experiment results. |
| `HW2_Ping_Pong/`     | Ping Pong agent with rule enhancements and experiments using multiple KNN models. |
| `HW3_Snake/`         | Snake game with KNN-based training and rule analysis. Focuses on model generalization and overfitting. |
| `HW4_CartPole/`      | Q-learning implementation for the CartPole balancing task. |
| `MLGame/`            | The game engine framework used for simulation and agent interaction. |
| `references/`        | Peer reports, alternative models, and experimental variations. |

---

## 5. Key Learnings

- Game-based ML tasks help visualize how models make decisions.
- Feature engineering plays a crucial role in the performance of simple ML models.
- Reinforcement learning provides a natural way to tackle decision-making without labeled datasets.
- Rule-based logic serves as a strong baseline for both evaluation and data generation.

---

## 6. Future Directions

- Expand to more advanced reinforcement learning methods like DQN.
- Integrate real-time visualizations and performance dashboards.
- Develop unified feature pipelines to enable transfer learning across games.
- Add interpretability components (e.g., SHAP, LIME) for understanding model behavior.

---

## 7. Author

**Name**: Liu Yi-An (劉翊安)  
**Affiliation**: National Cheng Kung University  
**GitHub**: [github.com/Liuian](https://github.com/Liuian)  
**LinkedIn**: *(Add link if available)*

