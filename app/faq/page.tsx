"use client"

import { useRouter } from "next/navigation"

export default function FAQPage() {
    const router = useRouter()

    return (
        <main className="flex flex-col items-center p-24 gap-4">
            <button onClick={() => router.push("/dashboard/testUser")}>Home</button>
            <h1>FAQ</h1>
        </main>
    )
}
