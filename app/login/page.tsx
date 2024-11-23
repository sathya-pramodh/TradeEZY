"use client";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const router = useRouter();

  return (
    <main className="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
      <div className="absolute top-6 left-6">
        <button
          onClick={() => router.push("/")}
          className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-medium hover:bg-indigo-700 transition-transform duration-300 ease-in-out hover:scale-105 shadow-lg"
        >
          ← Home
        </button>
      </div>

      <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-md">
        <form className="flex flex-col items-center gap-6">
          <h1 className="text-3xl font-bold text-indigo-600">Login</h1>
          <input
            className="w-full bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 p-3"
            type="text"
            placeholder="Username"
          />
          <input
            className="w-full bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 p-3"
            type="password"
            placeholder="Password"
          />
        </form>
        <button
          onClick={() => router.push("/dashboard/testUser")}
          className="mt-4 w-full px-6 py-3 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 transition-transform duration-300 ease-in-out"
        >
          Login
        </button>
        <p className="mt-4 text-sm text-gray-500 text-center">
          Don't have an account?{" "}
          <button
            onClick={() => router.push("/signup")}
            className="ml-4 text-white font-medium hover:underline"
          >
            Sign up
          </button>
        </p>
      </div>
    </main>
  );
}
