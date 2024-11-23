"use client";
import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();

  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex flex-col">
      {/* Header */}
      <header className="flex justify-between items-center px-12 py-6 bg-white shadow-md">
        <div className="text-2xl font-bold text-indigo-700">TradeEZY</div>
        <nav className="flex gap-6">
          <button
            onClick={() => router.push("/about")}
            className="bg-white text-indigo-500 hover:text-indigo-700 hover:bg-white hover:scale-110 transition-transform duration-300 ease-in-out px-5 py-2.5"
          >
            About
          </button>
          <button
            onClick={() => router.push("/faq")}
            className="bg-white text-indigo-500 hover:text-indigo-700 hover:bg-white hover:scale-110 transition-transform duration-300 ease-in-out px-5 py-2.5"
          >
            Features
          </button>
          <button
            onClick={() => router.push("/contact")}
            className="bg-white text-indigo-500 hover:text-indigo-700 hover:bg-white hover:scale-110 transition-transform duration-300 ease-in-out px-5 py-2.5"
          >
            Contact
          </button>
          <button
            onClick={() => router.push("/login")}
            className="px-4 py-2 text-indigo-500 bg-white border border-indigo-500 rounded-lg hover:bg-indigo-600 hover:text-white transition duration-300"
          >
            Login
          </button>
        </nav>
      </header>

      {/* Hero Section */}
      <section className="flex flex-col lg:flex-row items-center justify-between px-12 py-16 flex-grow">
        <div className="max-w-lg">
          <h1 className="text-4xl lg:text-5xl font-bold text-gray-800">
            Simplify Global Trade with{" "}
            <span className="text-indigo-600">AI-Driven Insights</span>
          </h1>
          <p className="mt-6 text-lg text-gray-600">
            TradeEZY is your trusted partner for international expansion.
            Navigate the complexities of cross-border trade with
            ease—compliance, incentives, shipping logistics, and market
            insights, all in one place.
          </p>
          <button
            onClick={() => router.push("/signup")}
            className="mt-8 px-6 py-3 bg-indigo-600 text-white text-lg rounded-lg shadow-lg hover:bg-indigo-700"
          >
            Get Started
          </button>
        </div>
        <div className="mt-12 lg:mt-0 lg:ml-12">
          <img
            src="/images/tradeazy-image.jpg"
            alt="TradeEZY hero illustration"
            className="max-w-full h-auto"
          />
        </div>
      </section>

      {/* Features Section */}
      <section className="bg-white py-12">
        <div className="max-w-6xl mx-auto px-6 lg:px-12">
          <h2 className="text-3xl font-bold text-gray-800 text-center">
            Why Choose TradeEZY?
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-10">
            <div className="flex flex-col items-center text-center">
              <img
                src="/images/clipboard.png"
                alt="Compliance"
                className="w-16 h-16 mb-4"
              />
              <h3 className="text-xl font-semibold text-gray-700">
                Compliance Simplified
              </h3>
              <p className="mt-2 text-gray-600">
                Get tailored compliance checklists and step-by-step guidance for
                international trade.
              </p>
            </div>
            <div className="flex flex-col items-center text-center">
              <img
                src="/images/discount.png"
                alt="Cost Optimization"
                className="w-16 h-16 mb-4"
              />
              <h3 className="text-xl font-semibold text-gray-700">
                Cost Optimization
              </h3>
              <p className="mt-2 text-gray-600">
                Discover cost-effective shipping options and tax estimates for
                your shipments.
              </p>
            </div>
            <div className="flex flex-col items-center text-center">
              <img
                src="/images/insight.png"
                alt="Market Insights"
                className="w-16 h-16 mb-4"
              />
              <h3 className="text-xl font-semibold text-gray-700">
                Real-Time Insights
              </h3>
              <p className="mt-2 text-gray-600">
                Analyze market risks, competition, and business opportunities
                with dynamic dashboards.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section className="bg-gradient-to-br from-indigo-100 to-blue-50 py-16">
        <div className="max-w-6xl mx-auto px-6 lg:px-12 text-center">
          <h2 className="text-3xl font-bold text-gray-800">How It Works</h2>
          <div className="flex flex-col lg:flex-row justify-around items-center mt-10 gap-10">
            <div className="max-w-xs text-center">
              <img
                src="/images/exam.png"
                alt="Step 1"
                className="w-20 h-20 mx-auto mb-4"
              />
              <h3 className="text-xl font-semibold text-gray-700">
                1. Provide Details
              </h3>
              <p className="text-gray-600">
                Enter your target country, shipment details, and product type.
              </p>
            </div>
            <div className="max-w-xs text-center">
              <img
                src="/images/audience.png"
                alt="Step 2"
                className="w-20 h-20 mx-auto mb-4"
              />
              <h3 className="text-xl font-semibold text-gray-700">
                2. Get Insights
              </h3>
              <p className="text-gray-600">
                Receive compliance checklists, market insights, and cost
                estimates.
              </p>
            </div>
            <div className="max-w-xs text-center">
              <img
                src="/images/international.png"
                alt="Step 3"
                className="w-20 h-20 mx-auto mb-4"
              />
              <h3 className="text-xl font-semibold text-gray-700">
                3. Expand Globally
              </h3>
              <p className="text-gray-600">
                Leverage our tools to simplify international trade and scale
                easily.
              </p>
            </div>
          </div>
        </div>
      </section>

      <footer className="bg-white shadow-md py-2 text-center text-gray-600">
        <nav className="flex justify-center gap-3 mt-2">
          <button
            onClick={() => router.push("/faq")}
            className="px-4 py-2 text-indigo-500 bg-white border border-indigo-500 rounded-lg hover:bg-indigo-600 hover:text-white transition duration-300"
          >
            FAQs
          </button>
          <button
            onClick={() => router.push("/contact")}
            className="px-4 py-2 text-indigo-500 bg-white border border-indigo-500 rounded-lg hover:bg-indigo-600 hover:text-white transition duration-300"
          >
            Contact Us
          </button>
        </nav>
        <p className="mt-4 text-center">© 2024 TradeEZY. All rights reserved.</p>
      </footer>
    </main>
  );
}
