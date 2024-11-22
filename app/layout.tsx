import './globals.css'
import { Inter } from 'next/font/google'
import Providers from './providers'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
    title: 'TradeEZY',
    description: 'TradeEZY is an AI-driven platform designed to help e-commerce businesses streamline their international expansion by simplifying the complexities of cross-border regulations, compliance, government incentives, shipping logistics, and market insights.',
}

export default function RootLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <html lang="en">
            <body className={inter.className}>
                <Providers children={children} />
            </body>
        </html>
    )
}
