"use client";
import { useEffect, useState } from "react";

export default function History() {
  const [history, setHistory] = useState<any[]>([]);

  useEffect(() => {
    const saved = JSON.parse(localStorage.getItem("history") || "[]");
    setHistory(saved);
  }, []);

  const view = (item: any) => {
    localStorage.setItem("selected", JSON.stringify(item));
    window.location.href = "/detection";
  };

  const clearAll = () => {
    localStorage.removeItem("history");
    setHistory([]);
  };

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
            <a href="/history" className="nav-link nav-active">History</a>
          </nav>
        </div>
      </header>

      <main className="content">
        <h1 className="page-title">Analysis History</h1>

        {history.length === 0 ? (
          <p>No history yet.</p>
        ) : (
          <table className="history-table">
            <thead>
              <tr>
                <th>News</th>
                <th>Verdict</th>
                <th>Confidence</th>
                <th>Date</th>
                <th></th>
              </tr>
            </thead>

            <tbody>
              {history.map((item, i) => (
                <tr key={i}>
                  <td>{item.inputShort}</td>
                  <td>
                    <span className={item.verdict === "REAL" ? "badge-real" : "badge-hoax"}>
                      {item.verdict}
                    </span>
                  </td>
                  <td>{item.confidence}%</td>
                  <td>{item.date}</td>
                  <td>
                    <button
                      className="btn-primary"
                      style={{ padding: "6px 12px" }}
                      onClick={() => view(item)}
                    >
                      View
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}

        <button className="btn-primary" style={{ marginTop: 20 }} onClick={clearAll}>
          Clear All
        </button>
      </main>
    </div>
  );
}
