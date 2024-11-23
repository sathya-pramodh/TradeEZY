"use client";

import { useRouter } from "next/navigation";

export default function FAQPage() {
    const router = useRouter();

    const faqList = [
        {
            question: "What is TradeEZY?",
            answer: "TradeEZY is an AI-powered consultant designed to simplify international business expansion by assisting with logistics, compliance, and market insights."
        },
        {
            question: "How does the chatbot assist with compliance?",
            answer: "The chatbot provides tailored compliance guidance by identifying required documents, mapping regulations, and offering a step-by-step checklist for the target country."
        },
        {
            question: "What is CRAT, and how does it work?",
            answer: "CRAT is a translation framework that ensures precise translations of industry-specific terms using a multi-agent framework and retrieval-augmented translation."
        },
        {
            question: "Does TradeEZY support real-time market insights?",
            answer: "Yes, TradeEZY offers real-time competitor analysis, market trends, and risk assessments using dynamic dashboards."
        },
        {
            question: "How do I access shipping cost estimates?",
            answer: "By providing shipment details, TradeEZY calculates and ranks the most cost-effective shipping modes, including taxes and fees."
        },
    ];

    return (
        <main className="min-h-screen p-6 bg-gradient-to-b from-indigo-100 via-white to-indigo-50">
            <div className="max-w-4xl mx-auto">
                <h1 className="text-4xl font-bold text-center text-indigo-600 mb-8">FAQs</h1>
                <div className="space-y-6">
                    {faqList.map((faq, index) => (
                        <div key={index} className="border-b pb-4">
                            <h2 className="text-lg font-semibold text-indigo-700">{faq.question}</h2>
                            <p className="text-gray-700 mt-2">{faq.answer}</p>
                        </div>
                    ))}
                </div>
                <button
                    onClick={() => router.push("/dashboard/testUser")}
                    className="mt-8 px-6 py-3 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 transition duration-300"
                >
                    Back to Home
                </button>
            </div>
        </main>
    );
}
