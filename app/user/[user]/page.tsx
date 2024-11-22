"use client"
import { useRouter } from "next/navigation"
import React, { Usable } from "react"

interface PageParams {
    user: string
}

export default function UserPage({ params }: { params: Usable<PageParams> }) {
    const user = React.use(params).user
    const router = useRouter()

    return (
        <main className="flex flex-col items-center p-24 gap-4">
            <button onClick={() => router.push("/faq")}>FAQ</button>
            <h1> Hi {user}! </h1>
            <form className="flex flex-col items-center gap-4">
                <select className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    <option>Product Category 1</option>
                    <option>Product Category 2</option>
                    <option>Product Category 3</option>
                </select>
                <select className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    <option>Target Market 1</option>
                    <option>Target Market 2</option>
                    <option>Target Market 3</option>
                </select>
                <button>Search</button>
            </form>
        </main>
    )
}
