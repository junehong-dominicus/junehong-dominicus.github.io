# SmartShopper policy publication gates

This PR adds a dedicated page without replacing or changing the website/AdSense policy. Do not merge and publish this review draft as the final app policy.

- [ ] June approves the wording and confirms `junehong.dominicus@gmail.com` as a monitored privacy contact (currently only seen as the Play listing contact).
- [ ] Verify the actual released AAB/APK, including active internal build 2 and Alpha build 4, or scope and verify a replacement release. Main source versionCode 5 does not establish shipped behavior.
- [ ] Verify merged manifest, SDK versions/configuration and runtime SDK/network behavior against the policy and Data safety answers. Source review found Ads 25.5.0 and ML Kit barcode 17.3.0.
- [ ] Verify Android cloud backup, device transfer, restoration/deletion behavior and provider retention/deletion request routes. No absolute local-only or instant-deletion promise is made.
- [ ] Verify the separate Android privacy-menu PR on device; only then change the planned-update paragraph into present-tense facts.
- [ ] Align target audience/Families with June's confirmed adult-shopping purpose. A 3+ content rating is not an audience declaration.
- [ ] Replace draft status/date with the approved effective date, remove review-only caveats, and remove `noindex` only after the final policy is approved. Do not remove substantive uncertainty without evidence.
- [ ] After merging the approved page, open the deployed app-specific URL, inspect its content, then use that exact live URL for the app and Play Console in a separate authorized step. The Android PR must not ship with a draft or missing destination.

No Play Console, Data safety, countries, release, publishing, ad identifiers, website policy, or GitHub Secrets are changed. June retains the existing 178-country choice; this PR does not implement Console settings.

Sources reviewed 2026-10-20:
- https://junehong-dominicus.github.io/privacy-policy.html (existing website-only policy)
- https://developers.google.com/admob/android/privacy/play-data-disclosure
- https://developers.google.com/ml-kit/android-data-disclosure
- https://developers.google.com/admob/android/privacy
- SmartShopper-Android main source at 48199f5 (source only; not binary certification).
