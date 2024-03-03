"use client"

import { useEffect, useState } from "react";
import { ref, onValue } from "firebase/database";  
import { database} from "@/lib/db";

interface ParkingSpace {
  slot: string;
  update: string; 
}

interface ParkingData {
  [key: string]: ParkingSpace;
}

export default function useParkingData() {
  const [parkingData, setParkingData] = useState<ParkingData>({});

  useEffect(() => {
    const parkingRef = ref(database);

    onValue(parkingRef, (snapshot) => {
      setParkingData(snapshot.val());
    });

  }, []);

  return parkingData;
}