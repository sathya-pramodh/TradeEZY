"use client"
import { useRouter } from "next/navigation";

export default function Home() {
    const router = useRouter();
    return (
        <main className="flex min-w-screen items-center justify-between p-12">
            <h1>Landing Page</h1>
            <button onClick={() => router.push("/login")}>Login</button>
        </main>
    )
}
