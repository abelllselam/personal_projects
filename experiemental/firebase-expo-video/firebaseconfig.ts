// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { initializeAuth, getReactNativePersistence } from "firebase/auth";
import ReactNativeAsyncStorage from "@react-native-async-storage/async-storage";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyA_ieOvZr-0Q_AIQHxoQYDuALC7Fxpg7Gw",
  authDomain: "fir-video-app-test.firebaseapp.com",
  projectId: "fir-video-app-test",
  storageBucket: "fir-video-app-test.firebasestorage.app",
  messagingSenderId: "456175019668",
  appId: "1:456175019668:web:25aeba745218635ecab681",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = initializeAuth(app, {
  persistence: getReactNativePersistence(ReactNativeAsyncStorage),
});
export const db = getFirestore(app);
export const storage = getStorage(app);
