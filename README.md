🧾 Resume Screening System (SVM-Based)
📋 Project Overview

This project is a Resume Classification System that automatically categorizes resumes into different job roles using TF-IDF (Term Frequency–Inverse Document Frequency) and a Support Vector Machine (SVM) model.

The system is deployed using FastAPI for backend APIs and a user-friendly web interface for interaction.

🖥️ Step 1: API Testing (Swagger UI)

Swagger UI is used to test the API endpoints.

It allows users to:

Upload resumes directly
Trigger the prediction API
Validate responses in real time

![Step1](assets/21.png) 

---

📊 Step 2: API Response

The API returns:

Predicted Job Category
Extracted Resume Text (Preview)

This helps in verifying both the classification result and the text extraction process.

![Step2](assets/22.png)

---

📤 Step 3: Upload Resume (Web UI)

A clean and user-friendly interface where users can upload resumes using:

Drag & Drop
File Browser

Supported file formats:

PDF
DOCX
TXT

![Step3](assets/23.png)

---

🔍 Step 4: Prediction Result

After clicking the Predict button:

The system processes the resume
Displays the predicted job category
Shows the extracted resume content

This provides transparency in how the model interprets the input.

![Step4](assets/24.png)

---

✍️ Step 5: Paste Text Option

Users can also:

Directly paste resume text
Get instant predictions without uploading files

This is useful for quick testing and debugging.

![Step5](assets/25.png) 

---

📂 Step 6: Supported Categories

The system displays all supported job categories, giving users a clear idea of classification scope.

![Step6](assets/26.png) 

---

⚙️ Tech Stack

FastAPI – Backend API development
Scikit-learn (SVM) – Machine learning model
TF-IDF – Feature extraction technique
HTML, CSS – Frontend interface

🚀 Key Highlights

End-to-end ML pipeline (text extraction → preprocessing → classification)
Real-time prediction via API and UI
Clean and intuitive user interface
Supports multiple resume formats
Easily extendable to more job categories
