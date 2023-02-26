package main

type BloomFilter interface {
	Add()
	Query()
}

type BloomF struct {
	M     uint
	K     uint
	P     float64
	Set   []byte
	hashF []HashWithSeed
}

func Create(n uint, p float64) *BloomF {
	m := CalculateM(int(n), p)
	k := CalculateK(int(n), m)
	hashF := CreateHashFunctions(k)
	bloomF := BloomF{m, k, p, make([]byte, m), hashF}
	return &bloomF
}

func (bloomF *BloomF) Add(elem string) {
	for _, hashFunc := range bloomF.hashF {
		i := hashFunc.Hash([]byte(elem))
		bloomF.Set[i] = 1
	}
}

func (bloomF *BloomF) Query(elem string) bool {
	for _, hashFunc := range bloomF.hashF {
		i := hashFunc.Hash([]byte(elem))
		if bloomF.Set[i] != 1 {
			return false
		}
	}
	return true
}
