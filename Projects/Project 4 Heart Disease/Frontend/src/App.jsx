import React from "react";
import HeartForm from "./HeartForm";

function App() {
  return (
    <>
      <div className="app-container">
        <h1 className="app-title">ML Use Case 4</h1>
        <HeartForm />
      </div>

      {/* CSS inside same file */}
      <style>{`
        .app-container {
          min-height: 100vh;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          background: linear-gradient(135deg, #e0f7fa, #f4f6f9);
          padding: 20px;
          font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        }

        .app-title {
          font-size: 2.2rem;
          font-weight: 700;
          margin-bottom: 25px;
          color: #2c3e50;
          text-align: center;
          text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        }
      `}</style>
    </>
  );
}

export default App;
