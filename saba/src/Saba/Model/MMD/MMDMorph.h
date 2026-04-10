//
// Copyright(c) 2016-2017 benikabocha.
// Distributed under the MIT License (http://opensource.org/licenses/MIT)
//

#ifndef SABA_MODEL_MMD_MMDMORPH_H
#define SABA_MODEL_MMD_MMDMORPH_H

#include <string>

namespace saba
{
	class MMDMorph
	{
	public:
		MMDMorph();

		void SetName(const std::string &name) { m_name = name; }
		const std::string &GetName() const { return m_name; }

		void SetWeight(float weight) { m_weight = weight; }
		float GetWeight() const { return m_weight; }

		void SaveBaseAnimation() { m_saveAnimWeight = m_weight; }
		void LoadBaseAnimation() { m_weight = m_saveAnimWeight; }
		void ClearBaseAnimation() { m_saveAnimWeight = 0; }
		float GetBaseAnimationWeight() const { return m_saveAnimWeight; }
		void SetManualControl(bool enable) { m_manualControl = enable; }
		bool IsManualControl() const { return m_manualControl; }
		void SetManualAnimationMorph(float weight, float blend_weight_set)
		{
			m_target_weight = weight;
			blend_weight = blend_weight_set;
		}

	public:
		std::string m_name;
		float blend_weight;
		float m_weight;
		float m_target_weight;
		float m_weight_vmd;
		float m_saveAnimWeight;
		bool m_manualControl = false;
	};
}

#endif // !SABA_MODEL_MMD_MMDMORPH_H
