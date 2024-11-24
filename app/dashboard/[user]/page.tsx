"use client";
import { useRouter } from "next/navigation";
import React from "react";

interface PageParams {
    user: string;
}

export default function UserPage({ params }: { params: Promise<PageParams> }) {
    const user = React.use(params).user;
    const router = useRouter();

    return (
        <main className="flex flex-col items-center min-h-screen bg-gradient-to-b from-indigo-100 via-white to-indigo-50 p-12">
            {/* Navigation Buttons */}
            <div className="flex gap-5 mb-8">
                <button
                    onClick={() => router.push("/faq")}
                    className="px-4 py-2 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 transition-transform duration-300 ease-in-out hover:scale-105"
                >
                    FAQ
                </button>
                <button
                    onClick={() => router.push("/login")}
                    className="px-4 py-2 bg-red-600 text-white font-medium rounded-lg hover:bg-red-700 transition-transform duration-300 ease-in-out hover:scale-105"
                >
                    Logout
                </button>
                <button
                    onClick={() => router.push("/upload")}
                    className="px-4 py-2 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 transition-transform duration-300 ease-in-out hover:scale-105"
                >
                    Upload
                </button>
            </div>

            {/* Greeting Section */}
            <h1 className="text-4xl font-bold text-indigo-600 mb-8">Hi, {user}!</h1>

            {/* Form Section */}
            <form className="bg-white rounded-lg shadow-lg p-8 w-full max-w-md flex flex-col gap-6">
                <h2 className="text-2xl font-semibold text-gray-700 mb-4">
                    Search Compliance
                </h2>

                {/* Product Category Select */}
                <select className="w-full bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 p-3">
                    <option>Product Category 1</option>
                    <option>Product Category 2</option>
                    <option>Product Category 3</option>
                </select>

                {/* Target Market Select */}
                <select className="w-full bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 p-3">
                    <option>Target Market 1</option>
                    <option>Target Market 2</option>
                    <option>Target Market 3</option>
                </select>

                {/* Search Button */}
                <button
                    onClick={() => router.push("/summary/compliance/testCompliance")}
                    className="w-full px-6 py-3 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 transition-transform duration-300 ease-in-out hover:scale-105"
                >
                    Search
                </button>
            </form>
        </main>
    );
}
