import { useState } from "react";
import axios from "axios";
import { FaHeartbeat, FaUser, FaTint, FaVial, FaRunning } from "react-icons/fa";
import { MdOutlineMonitorHeart } from "react-icons/md";

function HeartForm() {
  const [formData, setFormData] = useState({
    age: "",
    sex: "",
    trestbps: "",
    chol: "",
    thalach: "",
    oldpeak: "",
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await axios.post("http://localhost:5000/predict", formData);
      setPrediction(res.data.prediction);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="heart-container">
        <div className="heart-card">
          <h2 className="heart-title">
            <FaHeartbeat color="red" /> Heart Disease Predictor
          </h2>

          <form onSubmit={handleSubmit} className="heart-form">
            {/* Age */}
            <div className="form-group">
              <label>
                <FaUser /> Age
              </label>
              <input
                type="number"
                name="age"
                placeholder="Enter age"
                value={formData.age}
                onChange={handleChange}
                required
              />
            </div>

            {/* Sex */}
            <div className="form-group">
              <label>
                <FaUser /> Gender
              </label>
              <select
                name="sex"
                value={formData.sex}
                onChange={handleChange}
                required
              >
                <option value="">Select Gender</option>
                <option value="1">Male</option>
                <option value="0">Female</option>
              </select>
            </div>

            {/* Resting BP */}
            <div className="form-group">
              <label>
                <FaTint /> Resting Blood Pressure
              </label>
              <input
                type="number"
                name="trestbps"
                placeholder="mm Hg"
                value={formData.trestbps}
                onChange={handleChange}
                required
              />
            </div>

            {/* Cholesterol */}
            <div className="form-group">
              <label>
                <FaVial /> Cholesterol
              </label>
              <input
                type="number"
                name="chol"
                placeholder="mg/dl"
                value={formData.chol}
                onChange={handleChange}
                required
              />
            </div>

            {/* Max HR */}
            <div className="form-group">
              <label>
                <FaRunning /> Max Heart Rate
              </label>
              <input
                type="number"
                name="thalach"
                placeholder="bpm"
                value={formData.thalach}
                onChange={handleChange}
                required
              />
            </div>

            {/* Oldpeak */}
            <div className="form-group">
              <label>
                <MdOutlineMonitorHeart /> ST Depression
              </label>
              <input
                type="number"
                name="oldpeak"
                placeholder="Enter value"
                value={formData.oldpeak}
                onChange={handleChange}
                required
                step="0.1"
              />
            </div>

            {/* Submit Button */}
            <button type="submit" className="submit-btn">
              {loading ? "Predicting..." : "Predict"}
            </button>
          </form>

          {/* Prediction Result */}
          {prediction !== null && (
            <div
              className={`result ${
                prediction === 1 ? "result-danger" : "result-safe"
              }`}
            >
              {prediction === 1
                ? "High Risk of Heart Disease"
                : "Low Risk of Heart Disease"}
            </div>
          )}
        </div>
      </div>

      {/* CSS inside same file */}
      <style>{`
        .heart-container {
          min-height: 100vh;
          display: flex;
          justify-content: center;
          align-items: center;
          background: #f4f6f9;
          padding: 20px;
          font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
          text-align: center;
        }

        .heart-card {
          background: #fff;
          padding: 30px 25px;
          border-radius: 15px;
          box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
          width: 100%;
          max-width: 480px;
          transition: transform 0.2s ease-in-out;
        }

        .heart-card:hover {
          transform: translateY(-5px);
        }

        .heart-title {
          text-align: center;
          color: #222;
          font-size: 1.8rem;
          font-weight: 700;
          margin-bottom: 20px;
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 10px;
        }

        .heart-form .form-group {
          margin-bottom: 16px;
        }

        .heart-form label {
          display: flex;
          align-items: center;
          gap: 6px;
          font-weight: 600;
          margin-bottom: 6px;
          color: #333;
        }

        .heart-form input,
        .heart-form select {
          width: 100%;
          padding: 10px 12px;
          border: 1px solid #ccc;
          border-radius: 8px;
          outline: none;
          font-size: 14px;
          transition: border 0.3s ease;
        }

        .heart-form input:focus,
        .heart-form select:focus {
          border-color: #007bff;
        }

        .submit-btn {
          width: 100%;
          background: #007bff;
          color: white;
          font-size: 16px;
          font-weight: 600;
          padding: 12px;
          border: none;
          border-radius: 8px;
          cursor: pointer;
          transition: background 0.3s ease, transform 0.1s ease-in-out;
        }

        .submit-btn:hover {
          background: #0056b3;
        }

        .submit-btn:active {
          transform: scale(0.98);
        }

        .result {
          margin-top: 20px;
          padding: 14px;
          border-radius: 8px;
          font-size: 16px;
          font-weight: 600;
          text-align: center;
        }

        .result-danger {
          background: #ffe2e2;
          color: #d9534f;
          border: 1px solid #d9534f;
        }

        .result-safe {
          background: #e2ffe9;
          color: #28a745;
          border: 1px solid #28a745;
        }
      `}</style>
    </>
  );
}

export default HeartForm;
