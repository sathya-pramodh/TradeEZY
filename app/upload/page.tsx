"use client"
import { useRouter } from "next/navigation"
import React from "react"

export default function UserPage() {
    const router = useRouter()

    return (
        <main className="flex flex-col items-center p-24 gap-6">
            <button onClick={() => router.push("/dashboard/testUser")}>Home</button>
            <p>Upload document</p>
            <form className="flex flex-col gap-4">
                <input type="file" />
                <button>Upload</button>
            </form>
        </main>
    )
}
