# Resume_screening System
🧾 Resume Screening System using SVM
📋 Project Overview

This project develops an automated resume classification system using Natural Language Processing (NLP) and Support Vector Machines (SVM). The pipeline demonstrates how to transform raw resume text into structured features using TF-IDF vectorization and classify them into predefined job categories with high accuracy.

🛠️ Steps & Theory
Data Preprocessing & Cleaning

Loaded resume datasets and removed missing or inconsistent records.

Normalized text data by lowercasing, removing punctuation, and tokenizing content.

Performed stop word removal and custom cleaning to extract only meaningful tokens.

Feature Engineering

Used TF-IDF Vectorizer to convert text into numerical vectors, emphasizing unique and informative terms.

Encoded target labels using LabelEncoder for multi-class classification.

Model Building with SVM

Implemented a One-vs-Rest (OvR) SVM classifier to handle multiple job categories.

Tuned hyperparameters for optimal decision boundary and reduced overfitting.

Achieved high classification accuracy with consistent performance on validation data.

Model Saving & Deployment Ready

Saved the trained SVM model and TF-IDF vectorizer using pickle for seamless deployment.

Prepared scripts to accept new resumes and generate predictions in real-time.

✨ Key Highlights

End-to-End NLP Pipeline: From raw text to fully deployable classification model.

Custom Preprocessing: Removed noise and standardized resume data for improved accuracy.

Robust ML Model: Used SVM with OvR strategy to handle multi-class classification efficiently.

Deployment Ready: Packaged model and vectorizer for API/GUI integration.

🏁 Conclusion

This system provides a blueprint for automated resume screening solutions, demonstrating expertise in feature engineering, text classification, and deployment workflows. It showcases how TF-IDF + SVM can effectively classify unstructured resume data into relevant categories, reducing manual screening effort and improving hiring efficiency.
