import { database } from "@/lib/db";
import { ref, get as getFirebaseData} from "firebase/database";
import { NextResponse } from "next/server";

export async function GET() {
  try {
    const parkingRef = ref(database);

    const snapshot = await getFirebaseData(parkingRef);

    return NextResponse.json(snapshot.val(), { status: 200 });
  } catch (error: any) {
    return NextResponse.error();
  }
}
