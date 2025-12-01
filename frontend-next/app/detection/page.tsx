"use client";
import { useEffect, useState } from "react";

export default function Detection() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    const saved = localStorage.getItem("selected");
    if (saved) setData(JSON.parse(saved));
  }, []);

  if (!data) return <p>Loading...</p>;

  return (
    <div className="page-wrapper">
      <header>
        <div className="header-inner">
          <div>
            <div className="logo">JJN</div>
            <div className="tagline">Uncover the Truth</div>
          </div>
          <nav className="main-nav">
            <a href="/" className="nav-link">Home</a>
            <a href="/history" className="nav-link">History</a>
          </nav>
        </div>
      </header>

      <main className="content">
        <h1 className="page-title">Detection Result</h1>
        <p className="lead">{data.fullInput}</p>

        <div className="card">
          <h3>Verdict</h3>
          <div className={data.verdict === "REAL" ? "badge-real" : "badge-hoax"}>
            {data.verdict}
          </div>

          <h3>Confidence</h3>
          <p>{data.confidence}%</p>

          <div className="progress-bar">
            <div
              className="progress-fill"
              style={{
                width: `${data.confidence}%`,
                background: data.verdict === "REAL" ? "#31d67b" : "#ff4c4c",
              }}
            ></div>
          </div>
        </div>
      </main>
    </div>
  );
}
