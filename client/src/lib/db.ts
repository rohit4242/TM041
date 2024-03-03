// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  // apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  // authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  // projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  // storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  // messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  // appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
  // databaseURL: process.env.NEXT_PUBLIC_FIREBASE_DATABASE_URL,
  apiKey: "AIzaSyD2sqM7OQ5f6YOuydS3JKuMvrQtYBTrQP8",
  authDomain: "hackathon-cattle-detectio-2024.firebaseapp.com",
  databaseURL: "https://hackathon-cattle-detectio-2024-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "hackathon-cattle-detectio-2024",
  storageBucket: "hackathon-cattle-detectio-2024.appspot.com",
  messagingSenderId: "531733837767",
  appId: "1:531733837767:web:d0d65b1e3b7c562290cbe2",
  measurementId: "G-WC2P2MVNQD"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);


export { database }