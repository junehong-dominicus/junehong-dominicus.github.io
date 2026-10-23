# Snake Dice policy publication gates

This PR adds a dedicated page without replacing or changing the website/AdSense policy or the SmartShopper draft page. Do not merge and publish this review draft as the final app policy.

- [x] Privacy contact `junehong.dominicus@gmail.com` confirmed by June (WhatsApp 2026-10-20, same address as SmartShopper).
- [ ] Verify the actual release-candidate build (signed AAB from the CD workflow) against the policy and Data safety answers before publishing. Source review only; no shipped build exists yet.
- [ ] Verify merged manifest and SDK versions/configuration at build time (Google Mobile Ads 11.5.0 per Packages/manifest.json) and runtime ad behavior on a device (test ads still active; `useTestAdUnits` flips false at release).
- [ ] Verify the UMP consent form actually appears on device once a consent message is created in the AdMob console (Privacy & messaging); until then the consent paragraph describes required regions only.
- [ ] Verify on device that YouTube links and Settings/privacy controls sit behind the hold-to-open parent gate as described.
- [ ] Replace draft status/date with the approved effective date, remove review-only caveats, and remove `noindex` only after the final policy is approved.
- [ ] After merging the approved page, open the deployed URL, inspect it, then use that exact live URL in Play Console (and any in-app link) in a separate authorized step.

No Play Console, Data safety, ad units, release, or publishing settings are changed by this PR.

Sources reviewed 2026-10-20:
- https://developers.google.com/admob/android/privacy/play-data-disclosure
- https://developers.google.com/admob/unity/privacy (UMP / EU consent for the Unity plugin)
- https://support.google.com/googleplay/android-developer/answer/9893335 (Play Families policy requirements)
- mobile-game master at 8fcb897 (source only; not binary certification).
