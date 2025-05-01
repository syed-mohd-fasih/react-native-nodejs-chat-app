# 📱 Spam-o-tron

### "If it ain't spam, it ain't chat..."

## A secure, real-time chat application built with **React Native (Expo)** for the frontend and **Node.js** for the backend — featuring encryption, real-time messaging, and a clean monorepo structure using Git subtrees.

### 🧩 Project Structure

```plaintext
react-native-nodejs-chat-app/
├── frontend/   ← React Native app (Expo)
├── backend/    ← Node.js backend server
├── manage.py   ← Helper Python script to run both apps
└── README.md
```

## 🚀 How to Run the Project

### 📌 Requirements

-   Node.js (v18+)
-   Python 3 (to use the provided script)
-   Expo CLI: `npm install -g expo-cli`
-   MongoDB instance (local or cloud)
-   [Expo Go](https://expo.dev/client) app on your phone
-   Internet connection (for LAN-based development with Expo)

---

### ⚙️ Step 1: Set Up the Backend `.env`

Create a file named `.env` inside the `backend/` folder with the following content:

```env
PORT=3000
MONGO_DB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>?retryWrites=true&w=majority
JWT_SECRET=your-base64-secret-key
NODE_ENV=development
```

Make sure MongoDB is accessible and running.

---

### 📂 Step 2: Install Dependencies

```bash
# Frontend
cd frontend
npm install

# Backend
cd ../backend
npm install
```

---

### 🐍 Step 3: Run Both (frontend & backend) with Python Script

In the root directory, run:

```bash
python manage.py install
```

This will install all dependencies from the frontend and backend

```bash
python manage.py dev
```

This will automatically open two terminals:

-   One for the backend (`npm run dev`)
-   One for the frontend (`npx expo start`)

Ensure Python is added to your system PATH.

---

### ⚡ Optional: Run the App (Manually)

#### 🖥️ Start Backend

```bash
cd backend
npm run dev
```

#### 📲 Start Frontend (Expo)

```bash
cd frontend
npx expo start
```

#### Note: Use the **Expo Go** app on your phone to scan the QR code and launch the app.

---

## 🌳 Git Subtree Setup (for reference)

This monorepo uses Git **subtrees** to integrate separate frontend and backend repositories cleanly:

```bash
# Add frontend subtree
git remote add frontend-origin https://github.com/your-username/frontend-repo.git
git subtree add --prefix=frontend frontend-origin main --squash

# Add backend subtree
git remote add backend-origin https://github.com/your-username/backend-repo.git
git subtree add --prefix=backend backend-origin main --squash
```

You can later pull updates from the original repos:

```bash
git subtree pull --prefix=frontend frontend-origin main --squash
git subtree pull --prefix=backend backend-origin main --squash
```

---

## 🔐 Features

-   🔒 End-to-end encrypted messaging (RSA/AES)
-   ⚡ Real-time communication via WebSockets
-   👥 Authentication with JWT (or Firebase if used)
-   📁 Image/file sharing (optional)
-   🧠 Typing indicators & message delivery status

---

## 🛠 Tech Stack

| Layer    | Tech                           |
| -------- | ------------------------------ |
| Frontend | React Native (Expo)            |
| Backend  | Node.js, Express, WebSocket    |
| Auth     | JWT / Firebase (if applicable) |
| Database | MongoDB (Cloud/Local)          |
| Optional | Redis (pub/sub), Socket.IO     |

---

## 📜 License

This project is part of a semester submission and is not intended for production use.
