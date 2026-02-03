import { Helmet } from "react-helmet-async";
import React, { Suspense, lazy } from "react";
import Navbar from "@/components/Navbar";
import HeroSection from "@/components/HeroSection";
import Footer from "@/components/Footer";
import AnimatedBackground from "@/components/AnimatedBackground";
import WhatsAppButton from "@/components/WhatsAppButton";
import PointsMilestoneBanner from "@/components/PointsMilestoneBanner";

// Lazy loading components for Tirosh Performance Hacking
const AboutSection = lazy(() => import("@/components/AboutSection"));
const BoutiqueSection = lazy(() => import("@/components/BoutiqueSection"));
const AdvancedBookingSection = lazy(() => import("@/components/AdvancedBookingSection"));
const ContestSection = lazy(() => import("@/components/ContestSection"));
const AnonymousFeedback = lazy(() => import("@/components/AnonymousFeedback"));

const Index = () => {
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "BarberShop",
    "name": "TIROSH | Beauty & Hair Style",
    "image": "https://tirosh.co.il/logo.png",
    "description": "מספרת בוטיק אקסקלוסיבית בתל אביב.",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Tel Aviv",
      "addressCountry": "IL"
    }
  };

  return (
    <>
      <Helmet>
        <title>TIROSH | Luxury Barber & Boutique</title>
        <meta name="description" content="TIROSH - חוויית היוקרה המוחלטת לגבר המעודן." />
        <script type="application/ld+json">{JSON.stringify(jsonLd)}</script>
      </Helmet>

      <div className="min-h-screen bg-background relative overflow-x-hidden">
        <AnimatedBackground />
        <Navbar />
        
        <main className="relative z-10">
          <HeroSection />
          
          <Suspense fallback={<div className="h-20 animate-pulse bg-muted" />}>
            <AboutSection />
            <section id="contest"><ContestSection /></section>
            <section id="boutique"><BoutiqueSection /></section>
            <AdvancedBookingSection />
          </Suspense>
        </main>

        <Footer />
        <WhatsAppButton />
        <Suspense fallback={null}>
          <AnonymousFeedback />
        </Suspense>
        <PointsMilestoneBanner />
      </div>
    </>
  );
};

export default Index;
