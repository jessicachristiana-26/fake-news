"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Home() {
  const [text, setText] = useState("");
  const [url, setUrl] = useState("");
  const router = useRouter();

  const analyze = () => {
    if (!text && !url) {
      alert("Enter text or URL.");
      return;
    }

    const input = text || url;

    const confidence = Math.floor(Math.random() * 100) + 1;
    const verdict = confidence >= 60 ? "REAL" : "FAKE";

    const result = {
      fullInput: input,
      inputShort: input.slice(0, 60) + "...",
      confidence,
      verdict,
      date: new Date().toLocaleString(),
    };

    // save history
    let history = JSON.parse(localStorage.getItem("history") || "[]");
    history.unshift(result);
    localStorage.setItem("history", JSON.stringify(history));

    // save selected result
    localStorage.setItem("selected", JSON.stringify(result));

    router.push("/detection");
  };

  return (
    <>
      <header>
        <div className="header-inner">
          <div>
            <div className="logo">JJN</div>
            <div className="tagline">Uncover the Truth</div>
          </div>

          <nav className="main-nav">
            <a href="/" className="nav-link nav-active">Home</a>
            <a href="/history" className="nav-link">History</a>
          </nav>
        </div>
      </header>

      <main className="content">
        <h1 className="page-title">Uncover the Truth</h1>
        <p className="lead">Paste text or enter URL to analyze.</p>

        <div className="card">
          <textarea
            placeholder="Enter news text..."
            value={text}
            onChange={(e) => setText(e.target.value)}
          />

          <input
            placeholder="Or enter URL"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />

          <button className="btn-primary" onClick={analyze}>Analyze</button>
        </div>
      </main>
    </>
  );
}
