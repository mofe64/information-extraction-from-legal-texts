"use client";
export default function Results() {
  let info = [];
  if (typeof window !== "undefined") {
    info = JSON.parse(sessionStorage.getItem("info")) || [];
  }

  return (
    <div className="min-h-screen p-10">
      <h1>Results page</h1>
      {info.map((item) => {
        <p>{item} </p>;
        <br></br>;
      })}
    </div>
  );
}
