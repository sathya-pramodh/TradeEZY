"use client"
import { useRouter } from "next/navigation"
import React from "react"

interface PageParams {
    compliance: string
}

export default function CompliancePage({ params }: { params: Promise<PageParams> }) {
    const compliance = React.use(params).compliance
    const router = useRouter()

    return (
        <main className="flex flex-col items-center p-24 gap-4">
            <div className="flex">
                <button onClick={() => router.push("/dashboard/testUser")}>Home</button>
                <button onClick={() => router.push("/summary/grant/testGrant")}>Next</button>
            </div>
            <h1> {compliance} summary </h1>
        </main>
    )
}
