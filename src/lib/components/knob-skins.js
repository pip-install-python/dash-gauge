/**
 * Simplified implementation of knob skins inspired by react-rotary-knob-skin-pack
 * This implementation avoids dependency issues with the original skin pack
 */

// Import skin definitions
import s1 from './skins/s1';
import s5 from './skins/s5';
import s10 from './skins/s10';
import s15 from './skins/s15';

// Map of all available skins
const skins = {
  s1,
  s5,
  s10,
  s15
};

// Default skin
const defaultSkin = skins.s1;

// Helper to get a skin by name with fallback to default
const getSkin = (skinName) => {
  return skins[skinName] || defaultSkin;
};

export {
  skins,
  defaultSkin,
  getSkin
};