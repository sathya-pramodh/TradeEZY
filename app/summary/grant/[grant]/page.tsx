"use client"
import { useRouter } from "next/navigation"
import React from "react"

interface PageParams {
    grant: string
}

export default function GrantPage({ params }: { params: Promise<PageParams> }) {
    const grant = React.use(params).grant
    const router = useRouter()

    return (
        <main className="flex flex-col items-center p-24 gap-4">
            <div className="flex">
                <button onClick={() => router.push("/summary/compliance/testCompliance")}>Previous</button>
                <button onClick={() => router.push("/dashboard/testUser")}>Home</button>
            </div>
            <h1> {grant} summary </h1>
        </main>
    )
}
