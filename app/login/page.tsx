"use client"
import { useRouter } from "next/navigation"

export default function LoginPage() {
    const router = useRouter()

    return (
        <main className="flex items-center min-h-screen flex-col p-24 gap-6">
            <button onClick={() => router.push("/")}>Home</button>
            <form className="flex flex-col items-center gap-6">
                <h1>Login</h1>
                <input className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" type="text" />
                <input className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" type="password" />
                <button onClick={() => router.push("/dashboard/testUser")}>Login</button>
            </form>
        </main>
    )
}
