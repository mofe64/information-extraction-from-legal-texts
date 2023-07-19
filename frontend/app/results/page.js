"use client";
import { useEffect, useState } from "react";
export default function Results() {
  const [info, setInfo] = useState([]);
  console.log("info is " + info.length);

  useEffect(() => {
    const loadedInfo = JSON.parse(sessionStorage.getItem("info"));
    console.log(loadedInfo.info);
    setInfo(loadedInfo.info);
  }, []);

  return (
    <div className="min-h-screen p-10">
      <h1>Results page</h1>
      {info.map((item, i) => {
        return (
          <div className="my-4 p-2">
            <div className="flex">
              <p className="mr-2">{i + 1}.</p>
              <p>{item} </p>
            </div>
          </div>
        );
      })}
    </div>
  );
}
