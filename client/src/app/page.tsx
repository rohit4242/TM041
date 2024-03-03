"use client";

import axios from "axios";
import { useEffect, useState } from "react";

export default function Home() {
  const [slots, setSlots] = useState<{ [key: string]: any }>({});

  useEffect(() => {
    const interval = setInterval(() => {
      fetchSlots();
    }, 1000); // poll every 1 second

    return () => clearInterval(interval);
  }, []);

  const fetchSlots = async () => {
    const res = await axios.get("http://localhost:3000/api/slots");
    setSlots(res.data);
  };
  return (
    <div>
      <h1 className=" text-center text-6xl font-medium py-8">
        Cattle Detection{" "}
      </h1>
      <div className="grid grid-cols-5 gap-4 m-4">
        {Object.keys(slots).map((key) => {
          const detection = slots[key].cow_detection;
          const status = slots[key].status;
          console.log(detection)
          return (
            <div
              className={`p-4 rounded-md shadow-md ${
                detection ? "bg-teal-500" : "bg-rose-500"
              }`}
              key={key}
            >
              <h3 className="font-bold">{key}</h3>
              <p>Status: {status}</p>
              <p>Last updated: {slots[key].update_time}</p>
            </div>
          );
        })}
      </div>
    </div>
  );
}
