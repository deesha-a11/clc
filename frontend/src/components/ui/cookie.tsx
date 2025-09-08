"use client";

import { useEffect, useState } from "react";

export default function CookieConsent() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const consent = localStorage.getItem("cookieConsent");
    if (!consent) {
      setVisible(true);
    }
  }, []);

  const handleAccept = () => {
    localStorage.setItem("cookieConsent", "accepted");
    setVisible(false);
  };

  const handleDecline = () => {
    localStorage.setItem("cookieConsent", "declined");
    setVisible(false);
  };

  if (!visible) return null;

  return (
    <div className="fixed bottom-0 left-0 right-0 bg-gray-900 text-white p-4 shadow-lg flex flex-col md:flex-row justify-between items-center z-50">
      <p className="text-sm mb-2 md:mb-0">
        We use cookies to improve your browsing experience, analyze site traffic,
        and personalize content. By continuing, you agree to our{" "}
        <a href="/privacy-policy" className="underline">
          Privacy Policy
        </a>
        .
      </p>
      <div className="flex gap-2">
        <button
          onClick={handleDecline}
          className="px-4 py-2 bg-gray-600 rounded-lg hover:bg-gray-700"
        >
          Decline
        </button>
        <button
          onClick={handleAccept}
          className="px-4 py-2 bg-green-600 rounded-lg hover:bg-green-700"
        >
          Accept
        </button>
      </div>
    </div>
  );
}
